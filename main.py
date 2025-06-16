from src.generate_data import generate_fake_data
from src.process_data import process_data
from src.predict_trends import predict_sales

def run():
    print("Generating marketing data...")
    generate_fake_data()

    print("Processing data...")
    process_data()

    print("Predicting next 7 days of sales...")
    prediction = predict_sales()
    print(prediction)

if __name__ == "__main__":
    run()
