<template>
    <section>
        <base-card>
            <h2>Formulario chofer</h2>
            <chofer-form @guardar="guardarData" @editar="editarData"></chofer-form>
        </base-card>
    </section>
</template>

<script>
import ChoferForm from "../../components/chofer/ChoferForm.vue";
export default {
    components: {
        ChoferForm
    },
    methods: {
    guardarData(data) {
      this.$store.dispatch("choferes/agregarChofer", data);
      this.$router.replace("/choferes");
    },
    editarData(data) {
      this.$store.dispatch("choferes/editarChofer", data);
      this.$router.replace("/choferes");
    }
  }
}
</script>