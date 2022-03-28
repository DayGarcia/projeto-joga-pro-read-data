import functions.event as event
import functions.ticket as ticket


def main() -> bool:
    current_event_id = event.get_current_event_id()
    code = input("Insira o código do ingresso: ")
    user_id = input("Insira o ID do usuário: ")
    is_valid = ticket.is_valid(current_event_id, code, user_id)
    print(is_valid)
    return is_valid


if __name__ == "__main__":
    main()
