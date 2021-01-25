<template>
  <section>
    <base-card>
      <h2>Formulario Trayecto</h2>
      <trayecto-form @guardar="guardarData" @editar="editarData"></trayecto-form>
    </base-card>
  </section>
</template>

<script>
import TrayectoForm from '../../components/trayecto/TrayectoForm.vue';
export default {
  components: {
      TrayectoForm
  },
  methods: {
    guardarData(data) {
      this.$store.dispatch("trayectos/agregarTrayecto", data);
      this.$router.replace("/trayectos");
    },
    editarData(data) {
      this.$store.dispatch("trayectos/editarTrayecto", data);
      this.$router.replace("/trayectos");
    },
  },
};
</script>
