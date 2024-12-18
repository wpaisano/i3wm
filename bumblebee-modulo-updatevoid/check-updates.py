import subprocess
import core.module
import core.widget
import core.input

class Module(core.module.Module):
    def __init__(self, config, theme):
        super().__init__(config, theme, core.widget.Widget(self.update_widget))
        self._text = " 0"  # Texto inicial do widget com o ícone

    def update(self):
        try:
            # Executa o comando xbps-install para verificar atualizações
            result = subprocess.run(
                ["xbps-install", "-nuM"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )
            if result.returncode == 0:
                # Conta o número de linhas na saída
                updates = result.stdout.strip().count('\n')
                self._text = f" {updates}"  # Apenas o ícone e o número
            else:
                # Define mensagem de erro na barra
                self._text = " ?"  # Indica erro de forma discreta
        except Exception:
            self._text = " ?"

    def update_widget(self, widget):
        # Retorna o texto que será exibido no widget
        return self._text


