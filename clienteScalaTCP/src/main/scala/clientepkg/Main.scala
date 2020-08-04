package clientepkg

object Main {
  def main(args: Array[String]): Unit = {
    val pantalla = new GuiCliente()
    val controlador = new ControladorChat(pantalla)
  }
}
