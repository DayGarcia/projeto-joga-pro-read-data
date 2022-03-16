import database


def main():
    code = input("Enter the code of the event: ")
    user_id = input("Enter the user id: ")
    sql = "SELECT id FROM projetoevent_ticket WHERE code = '%s' and user_id = '%s' LIMIT 1" % (
        code, user_id)

    data = database.select(sql)
    if(len(data) == 0):
        print("Código ou usuário inválido")
    else:
        print("Usuário liberado!")


if __name__ == "__main__":
    main()
