from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
def all_reg_models(X_train,X_test,y_train,y_test):
    # defined Models
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "Gradient Boosting": GradientBoostingRegressor(),
        "XGBoost": XGBRegressor(),
        "LightGBM": LGBMRegressor(),
        "Ridge": Ridge(),
        "Lasso": Lasso(),
        "ElasticNet": ElasticNet(),
        "KNeighborsRegressor":KNeighborsRegressor(),
        "SVR":SVR(),
        "MLPRegressor":MLPRegressor()
    }
    results = {}
    for name, model in models.items():
        # Modeli eğitme
        model.fit(X_train, y_train)
        # Test seti üzerinde tahmin yapma
        predictions = model.predict(X_test)
        # MSE ve R^2 değerlerini hesaplama
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)  # MSE'nin karekökünü alarak RMSE hesaplama
        r2 = r2_score(y_test, predictions)
        # Sonuçları saklama
        results[name] = (mse, rmse, r2)

    # Sonuçları yazdırma
    for name, (mse, rmse, r2) in results.items():
        print(f"{name}: Average RMSE: {rmse:.2f}")
        print(f"{name}: R2: {r2:.2f}")

    # En iyi modeli bulma (En düşük MSE'ye göre)
    best_model_name = min(results, key=lambda x: results[x][0])
    best_model_mse, best_model_rmse, best_model_r2 = results[best_model_name]
    print(50*"*")
    print(f"\nBest Performing Model: {best_model_name} with Average RMSE: {best_model_rmse:.2f} and R2: {best_model_r2:.2f}")
