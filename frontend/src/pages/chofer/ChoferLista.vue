<template>
  <div>
    <base-card>
      <div>
        <base-button mode="outline" @click="cargarChoferes"
          >Refrescar</base-button
        >
        <base-button v-if="!isLoading" link to="/chofeRegistro">
          Registar Chofer
        </base-button>
      </div>
      <div v-if="isLoading">
        <base-spinner></base-spinner>
      </div>
      <br />
      <table v-if="!isLoading">
        <tr>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>rut</th>
          <th>ubicación</th>
          <th>Vigencia</th>
          <th>Acción</th>
        </tr>
        <chofer-item
          v-for="chofer in choferes"
          :key="chofer.id"
          :id="chofer.id"
          :nombre="chofer.nombre"
          :apellido="chofer.apellido"
          :rut="chofer.rut"
          :ubicacion="chofer.lugar.LGR_NOMBRE"
          :vigencia="chofer.vigencia"
          @recargar-choferes="cargarChoferes"
        >
        </chofer-item>
      </table>
    </base-card>
  </div>
</template>

<script>
import ChoferItem from "../../components/chofer/ChoferItem.vue";
export default {
  data() {
    return {
      isLoading: false,
    };
  },
  components: {
    ChoferItem,
  },
  computed: {
    choferes() {
      return this.$store.getters["choferes/choferes"];
    },
  },
  created() {
    this.cargarChoferes();
  },
  methods: {
    async cargarChoferes() {
      this.isLoading = true;
      try {
        await this.$store.dispatch("choferes/cargarChoferes");
      } catch (error) {
        console.log(error);
      }
      this.isLoading = false;
    },
  },
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
