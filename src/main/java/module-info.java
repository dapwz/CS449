module dapwz.sosgame {
  requires javafx.controls;
  requires javafx.fxml;

  requires org.controlsfx.controls;
  requires com.dlsc.formsfx;
  requires org.kordamp.bootstrapfx.core;

  opens dapwz.sosgame to javafx.fxml;
  exports dapwz.sosgame;
}