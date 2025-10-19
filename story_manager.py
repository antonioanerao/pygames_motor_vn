import json
import importlib


class StoryManager:
    """
    Gerencia o fluxo narrativo do jogo (Visual Novel).
    Carrega o arquivo JSON de história, controla a cena atual,
    os blocos de diálogo, menus e a execução de ações dinâmicas.
    """

    def __init__(self, json_path="story/dialogo.json", start_scene="first_screen"):
        """
        Inicializa o gerenciador de história.
        Args:
            json_path (str): Caminho do arquivo JSON contendo a história.
            start_scene (str): Cena inicial a ser carregada.
        """
        with open(json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)  # Carrega o conteúdo completo do JSON

        self.current_scene = start_scene  # Nome da cena atual (chave no JSON)
        self.index = 0                    # Índice do bloco atual dentro da cena

    def get_block(self):
        """
        Retorna o bloco atual da cena (falas, textos e escolhas).
        Cada bloco é um dicionário do JSON.
        Returns:
            dict or None: O bloco atual, ou None se não existir.
        """
        scene = self.data.get(self.current_scene, [])
        return scene[self.index] if self.index < len(scene) else None

    def has_choices(self):
        """
        Verifica se o bloco atual possui opções de escolha (campo 'choices').

        Returns:
            bool: True se o bloco tem escolhas, False caso contrário.
        """
        block = self.get_block()
        return "choices" in block if block else False

    def get_choices(self):
        """
        Retorna a lista de escolhas disponíveis no bloco atual.
        Cada escolha é um dicionário contendo 'text', 'next' e/ou 'action'.

        Returns:
            list[dict]: Lista de opções de escolha (pode estar vazia).
        """
        return self.get_block().get("choices", []) if self.get_block() else []

    def next_block(self):
        """
        Avança para o próximo bloco dentro da cena atual.
        Usado para passar de uma fala para a seguinte.

        Returns:
            bool: True se conseguiu avançar, False se já estava no último bloco.
        """
        scene = self.data.get(self.current_scene, [])
        if self.index + 1 < len(scene):
            self.index += 1
            return True
        return False

    def goto(self, scene_name):
        """
        Altera a cena atual para outra, reiniciando o índice de bloco.

        Args:
            scene_name (str): Nome da nova cena (chave no JSON).
        """
        if scene_name in self.data:
            self.current_scene = scene_name
            self.index = 0
        else:
            print(f"[AVISO] Cena '{scene_name}' não encontrada no JSON.")

    def do_action(self, action_name, **kwargs):
        """
        Executa ações dinâmicas armazenadas em /actions/<action_name>.py
        Cada módulo deve conter uma função 'run(**kwargs)'.
        """
        try:
            # Importa o módulo da pasta /actions dinamicamente
            module = importlib.import_module(f"actions.{action_name}")

            # Verifica se o módulo possui a função 'run'
            if hasattr(module, "run"):
                module.run(**kwargs)
            else:
                print(f"[WARN] Ação '{action_name}' não tem função 'run()'")

        except ModuleNotFoundError:
            print(f"[WARN] Ação '{action_name}' não encontrada em /actions/")

        except Exception as e:
            print(f"[ERROR] Falha ao executar ação '{action_name}': {e}")
