<template>
  <tr>
    <td>{{ nReserva }}</td>
    <td>{{ nombre }}</td>
    <td>{{ apellido }}</td>
    <td>{{ rut }}</td>
    <td>
      <button class="btn danger" @click="deshabilitarPasajero">
        <i class="fa fa-trash"></i>
      </button>
      <button class="btn base" @click="editarPasajero">
        <i class="fa fa-list-ul"></i>
      </button>
    </td>
  </tr>
</template>

<script>
export default {
  props: ["id", "nombre", "apellido", "rut", "nReserva", "idPrograma"],
  emits: ["editar-pasajero"],
  computed: {
    urlEditar() {
      return `/programa/${this.idPrograma}/pasajeroEditar/${this.id}`;
    }
  },
  methods: {
    async deshabilitarPasajero() {
      try {
        await this.$store.dispatch("programas/deshabilitarPasajero", this.id);
      } catch (error) {
        console.log(error);
      }
      location.reload();
    },
    editarPasajero() {
      this.$router.replace(this.urlEditar);
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
