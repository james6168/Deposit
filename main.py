DEPOSIT_MONTH = [3, 6, 9, 12, 24, 18, 36]
MONTH_PERCENTS = {
    3: 0.035,
    6: 0.065,
    9: 0.075,
    12: 0.110,
    18: 0.115,
    24: 0.120,
    36: 0.125
}
MINIMAL_SUM = 5000
MAX_SUM = 500000


def get_input_sum():
    input_sum = int(input("Введите вашу сумму депозита: "))
    return input_sum


def get_input_product():
    input_product = int(input("Выберите кол-во месяцев для депозита: "))
    return input_product


def validate_deposit_month(input_product):
    if input_product not in DEPOSIT_MONTH:
        print("Выберите пожайлуста доступные продукты")


def validate_min_sum(input_sum):
    if input_sum < MINIMAL_SUM:
        print("Минимальная сумма депозита равна 5000")


def calculate_money_for_deposit(input_sum: int, month_count: int):
    percentage = MONTH_PERCENTS[month_count]
    total_sum = input_sum * percentage
    return total_sum


def calculate_money_during_month(user_id: int):
    from .db import user_accounts

    user = user_accounts[user_id]

    get_input_sum() * user.get_deposit() * user.get_last_percentage()


def write_user_in_db(user):
    from db import user_accounts
    user_accounts.append(user)
    print("Ваш счёт добавлен в учёт")


def main():
    from models import User
    from db import user_accounts
    last_user_id = user_accounts[-1].get_id()
    input_sum = get_input_sum()
    input_product = get_input_product()
    validate_min_sum(input_sum)
    validate_deposit_month(input_product)
    output_money_for_deposit = calculate_money_for_deposit(input_sum, input_product)
    print(output_money_for_deposit)

    just_created_user = User(last_user_id + 1, input_sum, MONTH_PERCENTS[input_product])

    user_accounts.append(just_created_user)
    print(user_accounts)
    print(just_created_user)


if __name__ == "__main__":
    main()