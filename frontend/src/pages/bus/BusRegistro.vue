<template>
  <section>
    <base-card>
      <h2>Formulario bus</h2>
      <bus-form @guardar="guardarData" @editar="editarData"></bus-form>
    </base-card>
  </section>
</template>

<script>
import BusForm from "../../components/bus/BusForm";

export default {
  components: {
    BusForm
  },
  methods: {
    guardarData(data) {
      this.$store.dispatch("buses/agregarBus", data);
      this.$router.replace("/buses");
    },
    editarData(data) {
      this.$store.dispatch("buses/editarBus", data);
      this.$router.replace("/buses");
    }
  }
};
</script>
