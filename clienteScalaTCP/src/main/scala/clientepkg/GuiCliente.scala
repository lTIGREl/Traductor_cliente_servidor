package clientepkg

import scala.swing._

class GuiCliente extends MainFrame {
  val enviar = new Button(text0 = "Traducir")
  val nom_ip = new Dimension(50, 20)
  val opciones = List("es-MX","en-US","pl-Pl","el-Gr","de-Al","fr-Fr","it-It")
  var lang_in = new ComboBox(opciones) {
    preferredSize = nom_ip
  }
  var lang_out = new ComboBox(opciones) {
    preferredSize = nom_ip
  }
  var ip_area = new TextField("127.0.0.1") {
    preferredSize = nom_ip
  }
  var mensaje_area = new TextField()
  var historial = new TextArea() {
    preferredSize = new Dimension(491, 500)
    editable = false
    visible = true
  }
  this.iniciarComponentes()

  def iniciarComponentes(): Unit = {
    resizable = false
    title = "Cliente Ubuntu/Scala"
    preferredSize = new Dimension(491, 324)
    visible = true
    contents = new TabbedPane {
      pages += new TabbedPane.Page("Datos", new BoxPanel(orientation = Orientation.Vertical) {

        contents += new BoxPanel(orientation = Orientation.Horizontal) {
          contents += new Label("Idioma (entrada)") {
            preferredSize = new Dimension(150, 0)
          }
          contents += lang_in
        }
        contents += new Separator(o = Orientation.Vertical){
          preferredSize = new Dimension(0, 20)
        }
        contents += new BoxPanel(orientation = Orientation.Horizontal) {
          contents += new Label("Idioma (salida)") {
            preferredSize = new Dimension(150, 0)
          }
          contents += lang_out
        }
        contents += new Separator(o = Orientation.Vertical){
          preferredSize = new Dimension(0, 20)
        }
        contents += new BoxPanel(orientation = Orientation.Horizontal) {
          contents += new Label("Ip de destino") {
            preferredSize = new Dimension(150, 0)
          }
          contents += ip_area
        }
        contents += new Separator(o = Orientation.Vertical) {
          preferredSize = new Dimension(0, 200)
        }
      }
      )
      //segunda página del tabbedpane
      pages += new TabbedPane.Page("Traducciones", new BoxPanel(orientation = Orientation.Vertical) {
        contents += historial
        contents += new BoxPanel(orientation = Orientation.Horizontal) {
          contents += mensaje_area
          contents += enviar
        }

      })
    }
  }
  peer.setLocationRelativeTo(null)
}
