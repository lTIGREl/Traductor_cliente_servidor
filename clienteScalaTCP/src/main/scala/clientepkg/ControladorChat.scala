package clientepkg
import scala.swing.event.ButtonClicked

class ControladorChat(nueva_pantalla: GuiCliente) {
  var pantalla: GuiCliente = null
  pantalla = nueva_pantalla
  var cliente = new Cliente()
  pantalla.visible = true
  pantalla.listenTo(pantalla.enviar)
  pantalla.reactions += {
    case ButtonClicked(b) if b == pantalla.enviar =>
      enviarMensaje()
  }

  def enviarMensaje(): Unit = {
    val hilo = new Thread {
      override def run {
        val cadena: String = s"${pantalla.lang_in.item}:${pantalla.lang_out.item}:${pantalla.mensaje_area.text}"
        cliente.inetAddress=pantalla.ip_area.text
        cliente.enviarMensaje(cadena)
        subirMensaje(pantalla.mensaje_area.text)
        subirRespuesta(cliente.respuesta)
      }
    }
    hilo.start()

  }

  def subirMensaje(mensaje: String): Unit = {
    pantalla.historial.append(s"${mensaje}\n")
    pantalla.mensaje_area.text = ""
  }

  def subirRespuesta(respuesta: String): Unit = {
    try pantalla.historial.append(s"$respuesta\n")
    catch {
      case ex: Exception =>
        println(s"Problema: ${ex.getMessage}")
    }
  }
}
