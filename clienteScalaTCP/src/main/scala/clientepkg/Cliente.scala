package clientepkg

import java.io.{DataInputStream, DataOutputStream, IOException}
import java.net._
import java.util.logging.{Level, Logger}

class Cliente() {
  var sock: Socket = null
  var mensaje: String = ""
  var port: Int = 6787
  var inetAddress: String = "127.0.0.1"
  var in: DataInputStream = null
  var out: DataOutputStream = null
  var respuesta: String = ""

  def enviarMensaje(texto: String): Unit = {
    try {
      this.sock = new Socket(this.inetAddress, this.port)
      this.in = new DataInputStream(this.sock.getInputStream())
      this.out = new DataOutputStream(this.sock.getOutputStream())
      out.writeUTF(texto)
      var chain = this.in.readAllBytes()
      this.respuesta = new String(chain,"UTF-8")
    } catch {
      case ex: Exception => println(s"Error1: ${ex.getMessage}")
    } finally {
      try {
        sock.close()
      } catch {
        case ex: Exception =>
      }
    }
  }
}