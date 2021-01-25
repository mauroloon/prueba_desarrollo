<template>
  <section>
    <base-card>
      <h2>Formulario Programa</h2>
      <programa-form
        @guardar="guardarData"
        @editar="editarData"
      ></programa-form>
      <br />
    </base-card>
  </section>
</template>

<script>
import ProgramaForm from "../../components/programa/ProgramaForm.vue";
export default {
  components: {
    ProgramaForm
  },
  methods: {
    guardarData(data) {
      this.$store.dispatch("programas/agregarPrograma", data);
      this.$router.replace("/programas");
    },
    editarData(data) {
      this.$store.dispatch("programas/editarPrograma", data);
      this.$router.replace("/programas");
    }
  }
};
</script>
