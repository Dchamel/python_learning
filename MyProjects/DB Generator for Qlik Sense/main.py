"""
qlik_data_generator.py

Генератор учебных данных для Qlik Sense в формате .xlsx.
Создаёт 5 реалистичных таблиц с ассоциациями для обучения аналитике:
- Customers
- Employees
- Targets
- Sales_Data
- Feedback

Автор: Denis Krivonosov
Лицензия: MIT
"""

import pandas as pd  # type: ignore
import numpy as np
from datetime import datetime, timedelta
import random
from pathlib import Path
from typing import List, Dict, Tuple, Optional


class QlikDataGenerator:
    """
    Класс для генерации учебных датасетов для Qlik Sense.

    Генерирует 5 таблиц в формате Excel (.xlsx):
    - Customers.xlsx
    - Employees.xlsx
    - Targets.xlsx
    - Sales_Data.xlsx
    - Feedback.xlsx

    Все данные согласованы по ключам (CustomerID, OrderID, Region и др.),
    что позволяет строить ассоциативные модели в Qlik.

    Атрибуты:
        output_dir (Path): Путь к папке для сохранения файлов.
        regions (List[str]): Список регионов.
        cities (Dict[str, List[str]]): Города по регионам.
        categories (List[str]): Категории товаров.
        products (Dict[str, List[str]]): Товары по категориям.
        segments (List[str]): Сегменты клиентов.
        years (List[int]): Годы для генерации.
        salespersons (List[str]): Имена менеджеров.
        departments (List[str]): Отделы сотрудников.
        managers (List[str]): Фамилии руководителей.
    """

    def __init__(self, output_dir: str = "qlik_training_data") -> None:
        """
        Инициализация генератора.

        Args:
            output_dir (str): Имя папки для сохранения файлов. По умолчанию 'qlik_training_data'.
        """
        self.output_dir: Path = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Справочники
        self.regions: List[str] = ["North", "South", "East", "West"]
        self.cities: Dict[str, List[str]] = {
            "North": ["Moscow", "St. Petersburg", "Vologda"],
            "South": ["Rostov", "Krasnodar", "Volgograd"],
            "East": ["Kazan", "Ufa", "Perm"],
            "West": ["Novosibirsk", "Omsk", "Tomsk"],
        }
        self.categories: List[str] = ["Electronics", "Accessories", "Software", "Peripherals"]
        self.products: Dict[str, List[str]] = {
            "Electronics": ["Laptop X1", "Tablet Z2", "Smartphone M5", "Monitor Pro"],
            "Accessories": ["Mouse Pro", "Keyboard K3", "Headset H7", "USB Hub"],
            "Software": ["Office Suite", "Antivirus Pro", "Analytics Tool"],
            "Peripherals": ["Webcam HD", "External SSD", "Docking Station"],
        }
        self.segments: List[str] = ["Corporate", "SME", "Startup", "Individual"]
        self.months: List[str] = [f"{i:02d}" for i in range(1, 13)]
        self.years: List[int] = [2022, 2023, 2024]
        self.salespersons: List[str] = ["Anna", "Boris", "Clara", "Denis", "Elena", "Fedor", "Gleb", "Helen"]
        self.departments: List[str] = ["Sales", "Marketing", "Support", "Finance"]
        self.managers: List[str] = ["Ivanov", "Petrov", "Sidorova", "Kuznetsov", "Smirnova"]

    def generate_customers(self, n: int = 500) -> pd.DataFrame:
        """
        Генерирует таблицу клиентов.

        Args:
            n (int): Количество клиентов. По умолчанию 500.

        Returns:
            pd.DataFrame: DataFrame с данными клиентов.
        """
        print("Генерация клиентов...")
        data: List[Dict[str, object]] = []
        for i in range(1, n + 1):
            region = random.choice(self.regions)
            city = random.choice(self.cities[region])
            segment = random.choice(self.segments)
            join_date = self.random_date(datetime(2020, 1, 1), datetime(2023, 12, 31))
            data.append({
                "CustomerID": f"C{str(i).zfill(3)}",
                "CustomerName": f"Client_{i:03d}",
                "City": city,
                "Region": region,
                "Segment": segment,
                "JoinDate": join_date.strftime("%Y-%m-%d"),
            })
        df = pd.DataFrame(data)
        df.to_excel(self.output_dir / "Customers.xlsx", index=False)
        return df

    def generate_employees(self, n: int = 200) -> pd.DataFrame:
        """
        Генерирует таблицу сотрудников.

        Args:
            n (int): Количество сотрудников. По умолчанию 200.

        Returns:
            pd.DataFrame: DataFrame с данными сотрудников.
        """
        print("Генерация сотрудников...")
        data: List[Dict[str, object]] = []
        for i in range(1, n + 1):
            name = random.choice(self.salespersons)
            department = random.choice(self.departments)
            manager = random.choice(self.managers)
            hire_date = self.random_date(datetime(2018, 1, 1), datetime(2023, 12, 31))
            salary = random.randint(50000, 120000)
            data.append({
                "EmployeeID": f"E{str(i).zfill(3)}",
                "Name": name,
                "Department": department,
                "Manager": manager,
                "HireDate": hire_date.strftime("%Y-%m-%d"),
                "Salary": salary,
            })
        df = pd.DataFrame(data)
        df.to_excel(self.output_dir / "Employees.xlsx", index=False)
        return df

    def generate_targets(self) -> pd.DataFrame:
        """
        Генерирует таблицу плановых показателей по регионам и месяцам.

        Returns:
            pd.DataFrame: DataFrame с планами продаж и прибыли.
        """
        print("Генерация планов...")
        data: List[Dict[str, object]] = []
        for year in self.years:
            for month in range(1, 13):
                for region in self.regions:
                    target_sales = random.randint(30000, 60000)
                    target_profit = int(target_sales * random.uniform(0.25, 0.35))
                    data.append({
                        "Region": region,
                        "Month": f"{month:02d}",
                        "Year": year,
                        "TargetSales": target_sales,
                        "TargetProfit": target_profit,
                    })
        df = pd.DataFrame(data)
        df.to_excel(self.output_dir / "Targets.xlsx", index=False)
        return df

    def generate_sales(self, n: int = 5000) -> pd.DataFrame:
        """
        Генерирует таблицу продаж с привязкой к клиентам и менеджерам.

        Args:
            n (int): Количество заказов. По умолчанию 5000.

        Returns:
            pd.DataFrame: DataFrame с данными продаж.
        """
        print("Генерация продаж...")
        customers_df = pd.read_excel(self.output_dir / "Customers.xlsx")
        data: List[Dict[str, object]] = []

        for i in range(1, n + 1):
            order_date = self.random_date(datetime(2022, 1, 1), datetime(2024, 2, 29))
            region = random.choice(self.regions)
            salesperson = random.choice(self.salespersons)
            customer = customers_df[customers_df["Region"] == region].sample(1).iloc[0]
            category = random.choice(self.categories)
            product = random.choice(self.products[category])
            quantity = random.randint(1, 10)
            unit_price = round(random.uniform(20, 1000), 2)
            total_sales = round(quantity * unit_price, 2)

            data.append({
                "OrderID": 1000 + i,
                "Date": order_date.strftime("%Y-%m-%d"),
                "Region": region,
                "SalesPerson": salesperson,
                "Product": product,
                "Category": category,
                "Quantity": quantity,
                "UnitPrice": unit_price,
                "TotalSales": total_sales,
                "CustomerID": customer["CustomerID"],
            })
        df = pd.DataFrame(data)
        df.to_excel(self.output_dir / "Sales_Data.xlsx", index=False)
        return df

    def generate_feedback(self, n: int = 3000) -> pd.DataFrame:
        """
        Генерирует отзывы клиентов на основе продаж.

        Args:
            n (int): Количество отзывов. По умолчанию 3000.

        Returns:
            pd.DataFrame: DataFrame с отзывами.
        """
        print("Генерация отзывов...")
        sales_df = pd.read_excel(self.output_dir / "Sales_Data.xlsx")
        data: List[Dict[str, object]] = []
        feedback_id = 1

        for _ in range(n):
            sale = sales_df.sample(1).iloc[0]
            rating = random.randint(1, 5)
            comment_options = {
                5: ["Отлично!", "Всё супер", "Рекомендую", "Быстрая доставка", "Качество на высоте"],
                4: ["Хорошо", "Всё нормально", "Есть мелкие недочёты", "Цена соответствует качеству"],
                3: ["Средне", "Можно лучше", "Доставка задержалась", "Поддержка медленная"],
                2: ["Разочарован", "Качество ниже ожиданий", "Не хватило товара"],
                1: ["Ужасно", "Не рекомендую", "Проблемы с поддержкой", "Долгая доставка"],
            }
            comment = random.choice(comment_options[rating])
            survey_date = self.random_date(
                datetime.strptime(sale["Date"], "%Y-%m-%d"),
                datetime.strptime(sale["Date"], "%Y-%m-%d") + timedelta(days=30)
            )

            data.append({
                "FeedbackID": f"F{str(feedback_id).zfill(3)}",
                "CustomerID": sale["CustomerID"],
                "OrderID": int(sale["OrderID"]),
                "Rating": rating,
                "Comment": comment,
                "SurveyDate": survey_date.strftime("%Y-%m-%d"),
            })
            feedback_id += 1

        df = pd.DataFrame(data)
        df.to_excel(self.output_dir / "Feedback.xlsx", index=False)
        return df

    @staticmethod
    def random_date(start: datetime, end: datetime) -> datetime:
        """
        Генерирует случайную дату в заданном диапазоне.

        Args:
            start (datetime): Начальная дата.
            end (datetime): Конечная дата.

        Returns:
            datetime: Случайная дата между start и end.
        """
        delta: timedelta = end - start
        random_days: int = random.randint(0, delta.days)
        return start + timedelta(days=random_days)

    def generate_all(self) -> None:
        """
        Полная генерация всех датасетов в правильном порядке зависимостей.
        """
        print("🚀 Запуск генерации всех датасетов...")
        self.generate_customers()
        self.generate_employees()
        self.generate_targets()
        self.generate_sales()
        self.generate_feedback()
        print(f"\n✅ Все файлы успешно сохранены в папку: {self.output_dir}")


# ================================
# Точка входа
# ================================

if __name__ == "__main__":
    generator = QlikDataGenerator(output_dir="qlik_training_data")
    generator.generate_all()
