import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 1. Dataset
data = [
    [2, 80, "Aylıq", 1],
    [24, 45, "İllik", 0],
    [5, 90, "Aylıq", 1],
    [36, 55, "İllik", 0],
    [12, 60, "Aylıq", 0],
    [3, 95, "Aylıq", 1],
    [48, 40, "İllik", 0],
    [8, 85, "Aylıq", 1],
    [18, 70, "İllik", 0],
    [1, 100, "Aylıq", 1],
    [30, 50, "İllik", 0],
    [15, 75, "Aylıq", 0],
    [6, 65, "Aylıq", 1],
    [42, 60, "İllik", 0],
    [10, 95, "Aylıq", 1],
    [20, 80, "İllik", 1],
    [28, 70, "Aylıq", 0],
    [4, 50, "Aylıq", 0],
    [32, 85, "İllik", 0],
    [7, 100, "Aylıq", 1],
    [16, 55, "Aylıq", 0],
    [9, 70, "Aylıq", 1],
    [26, 90, "İllik", 1],
    [40, 65, "İllik", 0]
]

df = pd.DataFrame(data, columns=["ay_sayi", "ayliq_odenis", "muqavile", "ayrilib"])
print(df.head())
print(df.dtypes)

# 2. Train/test split
X = df.drop(columns="ayrilib")
y = df["ayrilib"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print(X_train.shape, X_test.shape)

# Mətnlə birbaşa training etmək olmur.
model = LogisticRegression()
try:
    model.fit(X_train, y_train)
except ValueError as error:
    print(error)

# 3. StandardScaler
numerical_features = ["ay_sayi", "ayliq_odenis"]
print(X_train[numerical_features].describe())

scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
print("Ortalama:", scaler.mean_)
print("Standard deviation:", scaler.scale_)

X_train_scaled = scaler.transform(X_train[numerical_features])
print(X_train[numerical_features].head(3))
print(np.round(X_train_scaled[:3], 2))

scaled_df = pd.DataFrame(X_train_scaled, columns=numerical_features)
print(scaled_df.head())
print(scaled_df.mean().round(5))
print(scaled_df.std(ddof=0).round(5))

# fit_transform = fit + transform
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[numerical_features])
X_test_scaled = scaler.transform(X_test[numerical_features])
print(X_test_scaled[:3])

# 4. MinMaxScaler
minmax_scaler = MinMaxScaler()
X_train_minmax = minmax_scaler.fit_transform(X_train[numerical_features])
print(np.round(X_train_minmax[:5], 2))
print(X_train_minmax.min(axis=0))
print(X_train_minmax.max(axis=0))

# 5. Encoding
print(df["muqavile"].unique())
muqavile_encoded = df["muqavile"].map({"Aylıq": 0, "İllik": 1})
print(muqavile_encoded.head())
print(pd.get_dummies(df[["muqavile"]], dtype=int).head())

categorical_features = ["muqavile"]
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
X_train_encoded = encoder.fit_transform(X_train[categorical_features])
X_test_encoded = encoder.transform(X_test[categorical_features])
print(X_train_encoded[:5])
print(encoder.categories_)
print(encoder.get_feature_names_out())
print(pd.DataFrame(X_train_encoded, columns=encoder.get_feature_names_out()).head())
print(X_test_encoded)

# Unknown category
yeni_muqavile = pd.DataFrame({"muqavile": ["İki illik"]})
strict_encoder = OneHotEncoder(sparse_output=False)
strict_encoder.fit(X_train[categorical_features])
try:
    print(strict_encoder.transform(yeni_muqavile))
except ValueError as error:
    print(error)
print(encoder.transform(yeni_muqavile))

# 6. Data leakage — qəsdən səhv nümunələr
wrong_scaler = StandardScaler()
wrong_scaler.fit(X[numerical_features])
print("Bütün dataset:", wrong_scaler.mean_)
print("Training data:", scaler.mean_)

another_scaler = StandardScaler()
wrong_test_scaled = another_scaler.fit_transform(X_test[numerical_features])
print("Səhv:", np.round(wrong_test_scaled[:3], 2))
print("Düzgün:", np.round(X_test_scaled[:3], 2))

# 7. Manual preprocessing
X_train_processed = np.hstack((X_train_scaled, X_train_encoded))
X_test_processed = np.hstack((X_test_scaled, X_test_encoded))
print(X_train_processed.shape, X_test_processed.shape)
print(X_train_processed[:3])

manual_model = LogisticRegression()
manual_model.fit(X_train_processed, y_train)
predictions = manual_model.predict(X_test_processed)
print("Real nəticə:", y_test.to_numpy())
print("Prediction:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))

# 8. ColumnTransformer
preprocessor = ColumnTransformer([
    ("numerical", StandardScaler(), numerical_features),
    ("categorical", OneHotEncoder(handle_unknown="ignore", sparse_output=False),
     categorical_features)
])
X_train_transformed = preprocessor.fit_transform(X_train)
X_test_transformed = preprocessor.transform(X_test)
print(X_train_transformed[:5])
print(X_train_transformed.shape, X_test_transformed.shape)
print(np.allclose(X_train_processed, X_train_transformed))

feature_names = preprocessor.get_feature_names_out()
print(feature_names)
processed_df = pd.DataFrame(X_train_transformed, columns=feature_names)
print(processed_df.head())

# Qeyd edilməyən column-lar default olaraq silinir.
simple_preprocessor = ColumnTransformer([
    ("scaling", StandardScaler(), ["ayliq_odenis"])
])
result = simple_preprocessor.fit_transform(X_train)
print(result.shape)
print(result[:3])

# Passthrough column-u dəyişmədən saxlayır.
simple_preprocessor = ColumnTransformer([
    ("scaling", StandardScaler(), ["ayliq_odenis"])
], remainder="passthrough")
result = simple_preprocessor.fit_transform(X_train[numerical_features])
print(result[:3])
print(simple_preprocessor.get_feature_names_out())

# 9. Pipeline
pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", LogisticRegression())
])
pipeline.fit(X_train, y_train)
pipeline_predictions = pipeline.predict(X_test)
print("Real nəticə:", y_test.to_numpy())
print("Prediction:", pipeline_predictions)
print("Accuracy:", accuracy_score(y_test, pipeline_predictions))
print(np.array_equal(predictions, pipeline_predictions))

# 10. Inference
yeni_musteri = pd.DataFrame({
    "ay_sayi": [3],
    "ayliq_odenis": [90],
    "muqavile": ["Aylıq"]
})
print("Prediction:", pipeline.predict(yeni_musteri))
print("Probability:", pipeline.predict_proba(yeni_musteri))

yeni_musteriler = pd.DataFrame({
    "ay_sayi": [3, 36, 10],
    "ayliq_odenis": [90, 50, 70],
    "muqavile": ["Aylıq", "İllik", "İki illik"]
})
new_predictions = pipeline.predict(yeni_musteriler)
new_probabilities = pipeline.predict_proba(yeni_musteriler)
yeni_musteriler["prediction"] = new_predictions
yeni_musteriler["ayrilma_ehtimali"] = new_probabilities[:, 1].round(2)
print(yeni_musteriler)

# Pipeline daxilindəki preprocessing nəticəsi
print(pipeline.named_steps)
trained_preprocessor = pipeline.named_steps["preprocessing"]
print(trained_preprocessor.transform(
    yeni_musteriler[["ay_sayi", "ayliq_odenis", "muqavile"]]
))

# Yekun nümunə
musteri = pd.DataFrame({
    "ay_sayi": [6],
    "ayliq_odenis": [85],
    "muqavile": ["Aylıq"]
})
print("Prediction:", pipeline.predict(musteri))
print("Probability:", pipeline.predict_proba(musteri))
