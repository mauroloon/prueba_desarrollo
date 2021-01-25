<template>
  <section>
    <base-card>
      <h2>Ingresar pasajero</h2>
      <pasajero-form @guardar="guardarData"></pasajero-form>
      <br />
      <div v-if="isLoading">
        <base-spinner></base-spinner>
      </div>
      <table v-else-if="!modoEdit && !isLoading">
        <tr>
          <th>Número asiento</th>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Rut</th>
          <th>Acción</th>
        </tr>
        <pasajero-item
          v-for="pasajero in pasajeros"
          :key="pasajero.id"
          :id="pasajero.id"
          :idPrograma="idPrograma"
          :nombre="pasajero.nombre"
          :apellido="pasajero.apellido"
          :rut="pasajero.rut"
          :nReserva="pasajero.nReserva"
        ></pasajero-item>
      </table>
    </base-card>
  </section>
</template>

<script>
import PasajeroForm from "../../components/programa/PasajeroForm.vue";
import PasajeroItem from "../../components/programa/Pasajeroitem.vue";
export default {
  components: {
    PasajeroForm,
    PasajeroItem
  },
  data() {
    return {
      idPrograma: "",
      isLoading: false,
      modoEdit: false
    };
  },
  computed: {
    pasajeros() {
      return this.$store.getters["programas/pasajeros"];
    },
    urlProgramaPasajero() {
      return `/programa/${this.idPrograma}/pasajero`;
    }
  },
  created() {
    this.idPrograma = this.$route.params.id;
    this.cargarPasajeros();
  },
  methods: {
    guardarData(data) {
      this.$store.dispatch("programas/agregarPasajero", data);
      location.reload();
    },
    async cargarPasajeros() {
      this.isLoading = true;
      try {
        await this.$store.dispatch(
          "programas/cargarPasajeros",
          this.idPrograma
        );
      } catch (error) {
        console.log(error);
      }
      this.isLoading = false;
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
