import { createRouter, createWebHistory } from "vue-router";

import BusLista from "./pages/bus/BusLista.vue";
import BusRegistro from "./pages/bus/BusRegistro.vue";
import ChoferLista from "./pages/chofer/ChoferLista.vue";
import ChoferRegistro from "./pages/chofer/ChoferRegistro.vue";
import TrayectoLista from "./pages/trayecto/TrayectoLista.vue";
import TrayectoRegistro from "./pages/trayecto/TrayectoRegistro.vue";
import ProgramaLista from "./pages/programa/ProgramaLista.vue";
import ProgramaRegistro from "./pages/programa/ProgramaRegistro.vue";
import PasajeroRegistro from "./pages/programa/PasajeroRegistro.vue";
import PasajeroEditar from "./pages/pasajero/PasajeroRegistro.vue";

//TODO: CAMBIAR NOMBRES
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/buses" },
    { path: "/buses", component: BusLista },
    { path: "/busRegistro", component: BusRegistro },
    { path: "/busEditar/:id", component: BusRegistro },
    { path: "/choferes", component: ChoferLista },
    { path: "/chofeRegistro", component: ChoferRegistro },
    { path: "/choferEditar/:id", component: ChoferRegistro },
    { path: "/trayectos", component: TrayectoLista },
    { path: "/trayectoRegistro", component: TrayectoRegistro },
    { path: "/trayectoEditar/:id", component: TrayectoRegistro },
    { path: "/programas", component: ProgramaLista },
    { path: "/programaRegistro", component: ProgramaRegistro },
    { path: "/programaEditar/:id", component: ProgramaRegistro },
    { path: "/programa/:id/pasajero", component: PasajeroRegistro },
    {
      path: "/programa/:id/pasajeroEditar/:idPasajero",
      component: PasajeroEditar
    }
  ]
});

export default router;
