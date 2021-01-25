<template>
  <div>
    <section>
      <div class="card">
        <div>
          <base-button mode="outline" @click="cargarProgramas"
            >Refrescar</base-button
          >
          <base-button v-if="!isLoading" link to="/programaRegistro">
            Registar Programa
          </base-button>
        </div>
        <div v-if="isLoading">
          <base-spinner></base-spinner>
        </div>
        <br />
        <table>
          <tr>
            <th>Trayecto</th>
            <th>Fecha inicio</th>
            <th>Fecha llegada</th>
            <th>Bus</th>
            <th>Chofer</th>
            <th>Estado</th>
            <th>Vigencia</th>
            <th>Acción</th>
          </tr>
          <programa-item
            v-for="programa in programas"
            :key="programa.id"
            :id="programa.id"
            :trayecto="programa.trayecto"
            :fechaInicio="programa.fechaInicio"
            :fechaTermino="programa.fechaTermino"
            :bus="programa.bus"
            :chofer="programa.chofer"
            :estado="programa.estado"
            :vigencia="programa.vigencia"
            @recarga-programas="cargarProgramas"
          ></programa-item>
        </table>
      </div>
    </section>
  </div>
</template>

<script>
import ProgramaItem from "../../components/programa/ProgramaItem.vue";
export default {
  components: {
    ProgramaItem
  },
  data() {
    return {
      isLoading: false,
      error: null
    };
  },
  computed: {
    programas() {
      return this.$store.getters["programas/programas"];
    }
  },
  created() {
    this.cargarProgramas();
  },
  methods: {
    async cargarProgramas() {
      this.isLoading = true;
      try {
        await this.$store.dispatch("programas/cargarPrograma");
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
.card {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 80rem;
}
</style>
