def lists():
    linked_lists = [
        {
            "name": "Hotmail",
            "link": "https://www.hotmail.com"
        },
        {
            "name": "Gmail",
            "link": "https://www.gmail.com"
        },
        {
            "name": "Github",
            "link": "https://www.github.com"
        },
        {
            "name": "Yahoo",
            "link": "https://www.yahoo.com"
        },
        {
            "name": "OpenAI",
            "link": "https://www.openai.com"
        }
    ]
    return linked_lists

def adicionar_novo_link(list_links):
    print("Digite o nome do link:")
    nome = input()
    print("Digite o link:")
    link = input()
    list_links.append({
        "name": nome,
        "link": link
    })
    print("Link adicionado com sucesso!")
    
def pesquisar_link(list_links):
    print("Digite o nome do link:")
    nome = input()
    link_encontrado = False
    for link in list_links:
        if link["name"] == nome:
            print(link)
            link_encontrado = True
            break
    if not link_encontrado:
        print("Link não encontrado!")

def exibir_todos_link(list_links):
    for link in list_links:
        print(f"{link['name']}: {link['link']}")

def main():
    linked_lists = lists()
    opcao = 0
    while opcao != 4:
        print("O que você deseja fazer?")
        print("1. Adicionar um novo link")
        print("2. Exibir todos os links")
        print("3. Pesquisar por um link")
        print("4. Sair")
        print("Escolha uma opção:")
        opcao = int(input())
        if opcao == 1:
            adicionar_novo_link(linked_lists)
        elif opcao == 2:
            exibir_todos_link(linked_lists)
        elif opcao == 3:
            pesquisar_link(linked_lists)
        elif opcao == 4:
            print("Saindo...")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
