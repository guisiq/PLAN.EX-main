<template>
  <v-app>
<v-stepper v-model="e1">
    <v-stepper-header>
      <v-stepper-step
        :complete="e1 > 1"
        step="1"
      >
        variaveis 
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
        :complete="e1 > 2"
        step="2"
      >
        respostas
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3">
        resutado
      </v-stepper-step>
    </v-stepper-header>

    <v-stepper-items>
      <!-- variaveis -->
      <v-stepper-content step="1">
        <v-card
          class="mb-12"
          height="200px"
        >
          Números de variaveis :
          <v-text-field
              type="number"   
              step="any"
              min="0"
              ref="input"
              :rules="[numberRule]"
              v-model.number="Nvariaveis"
            ></v-text-field>
        
        </v-card>


        <v-btn text>
          Cancel
        </v-btn>
      
        <v-btn
          @click="voltar"
        >
          Voltar
        </v-btn>
        <v-btn
          color="primary"
          @click="avancar"
        >
          Continue
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>

        <v-btn
          color="primary"
          @click="e1 = 3"
        >
          Continue
        </v-btn>

        <v-btn text>
          Cancel
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="3">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>

        <v-btn
          color="primary"
          @click="e1 = 1"
        >
          Continue
        </v-btn>

        <v-btn text>
          Cancel
        </v-btn>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    e1: 1,
    Nvariaveis:0,
    numberRule: val => {
      if(val < 0) return 'insira um valor positivo '
      return true
    },
    avancar: ()=>{
      if (e1 <= 3) {
        e1++
      }
    },
    voltar: ()=>{
      if (e1 >= 0) {
        e1--
      }
    }
  }),
  meth
};
</script>
