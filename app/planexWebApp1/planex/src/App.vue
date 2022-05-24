<template>
  <v-app>
    <v-stepper v-model="tela">
      <v-stepper-header>
        <v-stepper-step
          :complete="tela > 1"
          step="1"
        >
          variaveis 
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
          :complete="tela > 2"
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
 
          >
            <label for="nVariaveisInput">Números de variaveis :</label>
            
            <v-text-field
                id="nVariaveisInput"
                type="number"   
                step="any"
                min="0"
                ref="input"
                
                :rules="[numberRule]"
                v-model.number="Nvariaveis"
              ></v-text-field>

              <!-- tabela -->
              <v-data-table
                :headers="headersVariaveis"
                :items="dsVariaveis"
                disable-pagination
                :hide-default-footer="true"
              >
                <!-- :footer-props="{
                  disablePagination:false

                }" -->
                
                <template v-slot:[`item.name`]="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.nome"
                    large
                    persistent
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    <div>{{ props.item.nome }}</div>
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        atualizar nome
                      </div>
                      <v-text-field
                        v-model="props.item.nome"
                        :rules="[max25chars]"
                        label="Edit"
                        single-line
                        counter
                        autofocus
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:[`item.unidade`]="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.unidade"
                    large
                    persistent
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    <div>{{ props.item.unidade }}</div>
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        atualizar unidade
                      </div>
                      <v-text-field
                        v-model="props.item.unidade"
                        :rules="[max25chars]"
                        label="Edit"
                        single-line
                        counter
                        autofocus
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:[`item.vBaixo`] ="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.vBaixo"
                    large
                    persistent
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    <div>{{ props.item.vBaixo }}</div>
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        atualizar vBaixo
                      </div>
                      <v-text-field
                        v-model="props.item.vBaixo"
                        :rules="[max25chars]"
                        label="Edit"
                        single-line
                        counter
                        autofocus
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:[`item.vAlto`] ="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.vAlto"
                    large
                    persistent
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    <div>{{ props.item.vAlto }}</div>
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        atualizar vAlto
                      </div>
                      <v-text-field
                        v-model="props.item.vAlto"
                        :rules="[max25chars]"
                        label="Edit"
                        single-line
                        counter
                        autofocus
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
              </v-data-table>
          
              <v-snackbar
                v-model="snack"
                :timeout="3000"
                :color="snackColor"
              >
                {{ snackText }}
          
                <template v-slot:action="{ attrs }">
                  <v-btn
                    v-bind="attrs"
                    text
                    @click="snack = false"
                  >
                    Close
                  </v-btn>
                </template>
              </v-snackbar>
          
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

        <v-stepper-content step="3">
          <v-card
            class="mb-12"
            color="grey lighten-1"
            height="200px"
          ></v-card>

          
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
      </v-stepper-items>
    </v-stepper>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  // https://codepen.io/duq/pen/PegPrJ
// https://thewebdev.info/2020/08/15/vuetify%E2%80%8A-%E2%80%8Aedit-table-content/
// https://www.codegrepper.com/code-examples/whatever/vuetify+editable+table
// https://www.codeply.com/p/CMcTQVlHvp/vuetify-editable-datatable
  name: 'App',

  data: () => ({
    tela: 1,
    Nvariaveis:0,
    snack: false,
    snackColor: '',
    snackText: '',
    headersVariaveis:[
      {
        text: "nome Variavel",
        align: "start",
        sortable: false,
        value: "name",
      },
      {
        text: "Unidade",
        align: "start",
        sortable: false,
        value: "unidade",
      },
      {
        text: "-1",
        align: "start",
        sortable: false,
        value: "vBaixo",
      },
      {
        text: "+1",
        align: "start",
        sortable: false,
        value: "vAlto",
      },
    ],
    dsVariaveis:[

    ],
    max25chars: v => v.length <= 25 || 'nome muito longo !',
   
  }),
  methods: {
    numberRule: val => {
      if(val < 0) return 'insira um valor positivo '
      return true
    },
    avancar() {
      console.log("passou por aqui");
      console.log("this.tela",this.tela);
      console.log("this.tela",this);

      if (this.tela <= 3) {
        this.tela++;
      }
      axios.get('https://api.coindesk.com/v1/bpi/currentprice.json');
    
    },
    voltar() {
      if (this.tela > 1) {
        this.tela--
      }
    },
    save () {
      this.snack = true
      this.snackColor = 'success'
      this.snackText = 'Data saved'
    },
    cancel () {
      this.snack = true
      this.snackColor = 'error'
      this.snackText = 'Canceled'
    },
    open () {
      this.snack = true
      this.snackColor = 'info'
      this.snackText = 'Dialog opened'
    },
    close () {
      console.log('Dialog closed')
    },
  },

  watch:{
    Nvariaveis(){
      console.log("alteracao");
      console.log("this.dsVariaveis:",this.dsVariaveis);
      if(this.dsVariaveis.length == this.Nvariaveis){
        console.log("this.dsVariaveis.length = N",this.dsVariaveis.length );
        console.log("this.dsVariaveis = N",this.dsVariaveis);
        return
      }else if(this.dsVariaveis.length > this.Nvariaveis){
        console.log("this.dsVariaveis.length > N",this.dsVariaveis.length );
        console.log("this.dsVariaveis > N",this.dsVariaveis);
         while (this.dsVariaveis.length != this.Nvariaveis) {

           this.dsVariaveis.splice(this.dsVariaveis.length -1,1);
         }

      }else if(this.dsVariaveis.length < this.Nvariaveis){
        console.log("this.dsVariaveis.length < N",this.dsVariaveis.length );

          while (this.dsVariaveis.length != this.Nvariaveis) {
            //let newVariavel =clone(this.dsVariaveis[1]);
            // console.log("this.dsVariaveis < N",this.dsVariaveis);
            // newVariavel.nome = "x" + this.dsVariaveis.length;
            this.dsVariaveis.push({
                                    nome: "x"+this.dsVariaveis.length ,
                                    unidade:" ",
                                    vBaixo:-1.0,
                                    vAlto:1.0
                                  }) ;
            
          }
      }
        
    }
  }

  
};
</script>
