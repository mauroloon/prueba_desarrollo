<template>
  <div>
    <base-card
      ><div>
        <base-button mode="outline" @click="recargar">Refrescar</base-button>
        <base-button
          v-if="!isLoading && !isLoadingLugares"
          link
          to="/trayectoRegistro"
        >
          Registar Trayecto
        </base-button>
      </div>
      <div v-if="isLoading && isLoadingLugares">
        <base-spinner></base-spinner>
      </div>
      <table v-else>
        <tr>
          <th>Origen</th>
          <th>Destino</th>
          <th>Vigencia</th>
          <th>Promedio pasajeros</th>
          <th>Acción</th>
        </tr>
        <trayecto-item
          v-for="trayecto in trayectos"
          :key="trayecto.id"
          :id="trayecto.id"
          :lugarInicial="trayecto.trayectoInicial"
          :lugarFinal="trayecto.trayectoFinal"
          :vigencia="trayecto.vigencia"
          :lugares="lugares"
          :promedio="trayecto.promedio"
          @recarga-trayectos="recargar"
        ></trayecto-item>
      </table>
    </base-card>
  </div>
</template>

<script>
import TrayectoItem from "../../components/trayecto/TrayectoItem.vue";
export default {
  components: {
    TrayectoItem
  },
  data() {
    return {
      isLoading: false,
      isLoadingLugares: false
    };
  },
  computed: {
    lugares() {
      return this.$store.getters["buses/lugares"];
    },
    trayectos() {
      return this.$store.getters["trayectos/trayectos"];
    }
  },
  created() {
    this.recargar();
  },
  methods: {
    recargar() {
      this.cargarLugares();
      this.cargarTrayectos();
    },
    async cargarTrayectos() {
      this.isLoading = true;
      try {
        await this.$store.dispatch("trayectos/cargaTrayectos");
      } catch (error) {
        console.log(error);
      }
      this.isLoading = false;
    },
    async cargarLugares() {
      this.isLoadingLugares = true;
      try {
        await this.$store.dispatch("buses/cargarLugares");
      } catch (error) {
        console.log(error);
      }
      this.isLoadingLugares = false;
    }
  }
};
</script>

<style scoped>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
