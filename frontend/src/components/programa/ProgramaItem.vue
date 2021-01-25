<template>
  <tr>
    <td>{{ trayecto }}</td>
    <td>{{ fechaInicioFormat }}</td>
    <td>{{ fechaTerminoFormat }}</td>
    <td>{{ bus }}</td>
    <td>{{ chofer }}</td>
    <td>{{ estado }}</td>
    <td>{{ programaVigente }}</td>
    <td>
      <button
        class="btn danger"
        v-if="deshabilitarBotton"
        @click="deshabilitarPrograma"
      >
        <i class="fa fa-trash"></i>
      </button>
      <button class="btn base" @click="editarPrograma">
        <i class="fa fa-list-ul"></i>
      </button>
      <button
        v-if="validarRegistroPasajero"
        class="btn success"
        @click="ingresarPasajero"
      >
        <i class="fa fa-calendar"></i>
      </button>
    </td>
  </tr>
</template>

<script>
import moment from "moment";
export default {
  props: [
    "id",
    "trayecto",
    "fechaInicio",
    "fechaTermino",
    "bus",
    "chofer",
    "estado",
    "vigencia"
  ],
  emits: ["recarga-programas"],
  computed: {
    programaVigente() {
      if (this.vigencia == 1) {
        return "Si";
      }
      return "No";
    },
    fechaInicioFormat() {
      return moment(String(this.fechaInicio)).format("DD-MM-YYYY HH:mm");
    },
    fechaTerminoFormat() {
      return moment(String(this.fechaTermino)).format("DD-MM-YYYY HH:mm");
    },
    urlEditar() {
      return `/programaEditar/${this.id}`;
    },
    urlPasajero() {
      return `/programa/${this.id}/pasajero`;
    },
    deshabilitarBotton() {
      if (this.vigencia == 1) {
        return true;
      }
      return false;
    },
    validarRegistroPasajero() {
      if (this.vigencia === 1 && this.estado === "Programado") {
        return true;
      }
      return false;
    }
  },
  methods: {
    editarPrograma() {
      this.$router.push(this.urlEditar);
    },
    ingresarPasajero() {
      this.$router.push(this.urlPasajero);
    },
    async deshabilitarPrograma() {
      try {
        await this.$store.dispatch("programas/deshabilitarPrograma", this.id);
      } catch (error) {
        console.log(error);
      }
      this.$emit("recarga-programas");
    }
  }
};
</script>

<style scoped>
td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

.btn {
  border: none;
  color: white;
  padding: 12px 16px;
  font-size: 16px;
  cursor: pointer;
}

.danger {
  background-color: #af0000;
}
.danger:hover {
  background-color: #ff0000;
}

.base {
  background-color: DodgerBlue;
}
.base:hover {
  background-color: rgb(0, 64, 255);
}

.success {
  background-color: #197e00;
}
.success:hover {
  background-color: #2cdb00;
}
</style>
