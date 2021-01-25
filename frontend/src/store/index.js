import { createStore } from "vuex";

import busModulo from "./modules/bus/index.js";
import choferModulo from "./modules/chofer/index.js";
import trayectoModulo from "./modules/trayecto/index.js";
import programaModulo from "./modules/programa/index.js"

const store = createStore({
  modules: {
    buses: busModulo,
    choferes: choferModulo,
    trayectos: trayectoModulo,
    programas: programaModulo
  }
});

export default store;
