import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "area_m2": [
        40, 45, 50, 55, 60,
        65, 70, 75, 80, 85,
        90, 95, 100, 105, 110,
        115, 120, 125, 130, 135
    ],
    "rooms": [
        1, 2, 1, 2, 2,
        3, 2, 3, 3, 2,
        3, 4, 3, 4, 3,
        4, 4, 3, 4, 5
    ],
    "price_azn": [
        73000, 81500, 82500, 98500, 97000,
        113700, 114500, 121100, 130700, 125800,
        142800, 149000, 155000, 163000, 165000,
        171900, 181800, 177500, 193500, 201700
    ]
}

df = pd.DataFrame(data)

x = df[["area_m2", "rooms"]] # Features
y = df["price_azn"] # Target

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42
)

model = LinearRegression()

model.fit(x_train, y_train)

predictions = model.predict(x_test)

comparison = pd.DataFrame({
    "real_price_azn": y_test.to_numpy(),
    "predicted_price_azn": predictions.round().astype(int)
})

comparison["error_azn"] = abs(
    comparison["real_price_azn"] - comparison["predicted_price_azn"]
)

print(comparison)
