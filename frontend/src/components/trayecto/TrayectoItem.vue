<template>
  <tr>
    <td>{{ lugarInicialNombre }}</td>
    <td>{{ lugarFinalNombre }}</td>
    <td>{{ trayectoVigente }}</td>
    <td>{{ promedio }}</td>
    <td>
      <button
        class="btn"
        v-if="deshabilitarBotton"
        @click="deshabilitarTrayecto"
      >
        <i class="fa fa-trash"></i>
      </button>
      <button class="btn" @click="editarTrayecto">
        <i class="fa fa-list-ul"></i>
      </button>
      <button class="btn" @click="listaBusesTrayecto">
        Bus
      </button>
    </td>
  </tr>
  <base-dialog :show="mostrar" titulo="Lista Buses" @close="cerrarDialog">
    <table v-if="validarTablaBuses">
      <tr>
        <th>Programa</th>
        <th>Bus</th>
        <th>Porcentaje vendido</th>
      </tr>
      <tr v-for="data in listaBuses" :key="data.reserva">
        <td>{{ data.reserva }}</td>
        <td>{{ data.bus }}</td>
        <td>{{ data.porcentaje }}%</td>
      </tr>
    </table>

    <p v-else>Sin datos para mostrar</p>
  </base-dialog>
</template>

<script>
export default {
  props: [
    "id",
    "lugarInicial",
    "lugarFinal",
    "vigencia",
    "lugares",
    "promedio"
  ],
  emits: ["recarga-trayectos"],
  data() {
    return {
      mostrar: false,
      listaBuses: []
    };
  },
  computed: {
    urlEditar() {
      return `/trayectoEditar/${this.id}`;
    },
    trayectoVigente() {
      if (this.vigencia == 1) {
        return "Si";
      }
      return "No";
    },
    deshabilitarBotton() {
      if (this.vigencia == 1) {
        return true;
      }
      return false;
    },
    lugarInicialNombre() {
      if (this.lugares.length > 0) {
        const lugar = this.lugares.find(
          element => element.id == this.lugarInicial
        );
        return lugar.nombre;
      } else {
        return "";
      }
    },
    lugarFinalNombre() {
      if (this.lugares.length > 0) {
        const lugar = this.lugares.find(
          element => element.id == this.lugarFinal
        );
        return lugar.nombre;
      } else {
        return "";
      }
    },
    validarTablaBuses() {
      if (this.listaBuses.length > 0) {
        return true;
      }
      return false;
    }
  },
  methods: {
    async deshabilitarTrayecto() {
      try {
        await this.$store.dispatch("trayectos/deshabilitarTrayecto", this.id);
      } catch (error) {
        console.log(error);
      }
      this.$emit("recarga-trayectos");
    },
    editarTrayecto() {
      this.$router.push(this.urlEditar);
    },
    listaBusesTrayecto() {
      this.mostrar = true;
      this.cargarBusesTrayecto();
    },
    cerrarDialog() {
      this.mostrar = false;
    },
    async cargarBusesTrayecto() {
      const response = await fetch(
        `http://localhost:8000/v1/bus/trayecto/${this.id}/buses/`
      );
      const responseData = await response.json();

      if (responseData.code == 1) {
        this.listaBuses = responseData.data;
      }
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
td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 16px;
  font-size: 16px;
  cursor: pointer;
}

.btn:hover {
  background-color: RoyalBlue;
}
</style>
