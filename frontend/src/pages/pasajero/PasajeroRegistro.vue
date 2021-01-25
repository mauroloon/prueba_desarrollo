<template>
  <base-card>
    <h1>pasajero form</h1>
    <pasajero-form
      @editar="EditarData"
      @cancelar="cancelarEdit"
    ></pasajero-form>
  </base-card>
</template>

<script>
import PasajeroForm from "../../components/pasajero/PasajeroForm.vue";
export default {
  components: {
    PasajeroForm
  },
  computed: {
    urlPrograma() {
      return `/programa/${this.$route.params.id}/pasajero`;
    }
  },
  methods: {
    EditarData(data) {
      this.$store.dispatch("programas/editarPasajero", data);
      this.$router.replace(this.urlPrograma);
    },
    cancelarEdit(url) {
      this.$router.replace(url);
    }
  }
};
</script>
