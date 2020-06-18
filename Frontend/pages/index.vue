<template>
  <v-layout>
    <v-row>
      <v-col cols="9">
        <v-card>
          <v-card-title>
            <span class="headline">Extract keywords from sample document</span>
            <div class="flex-grow-1"></div>
            <v-btn color="primary" @click="reload">Reload</v-btn>
          </v-card-title>
          <v-textarea
            filled
            name="input-7-4"
            label="Content"
            auto-grow
            v-model="textraw"
            :disabled="!isExtract"
          ></v-textarea>
        </v-card>

        <v-row>
          <!-- <v-col cols="3">
            <v-select label="Language" :items="lan" v-model="lan_req"></v-select>
          </v-col> -->
          <v-col cols="3">
            <v-select label="N-gram" :items="ngram" v-model="ngram_req"></v-select>
          </v-col>
          <!-- <v-col cols="3">
            <v-select label="Feauture" :items="feauture" v-model="feauture_req" attach multiple></v-select>
          </v-col> -->
          <v-col cols="3">
            <v-select label="Number of keywords" :items="numberOfWord" v-model="noW"></v-select>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-btn
              v-if="isExtract"
              class="primary"
              @click="extractDocument"
            >Extract important KeysWord</v-btn>

            <!-- <v-btn v-if="!isExtract" @click="change" class="primary">Re</v-btn> -->
          </v-col>
        </v-row>

        <v-row>
          <v-card v-if="!isExtract">
            <v-card-title>
              <span class="headline">Content</span>
            </v-card-title>
            <v-card-text filled v-html="dataRes.text"></v-card-text>
          </v-card>
        </v-row>
      </v-col>

      <v-col v-if="!isExtract" cols="3">
        <span class="headline">Keywords by Yake</span>
        <v-data-table
          :headers="headers"
          :items="items"
          hide-default-header
          hide-default-footer
          class="elevation-1"
        ></v-data-table>
      </v-col>
    </v-row>
  </v-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  components: {},
  data() {
    return {
      isExtract: true,
      keywords: [],
      lan: ["en", "vi"],
      noW: 5,
      numberOfWord: [5, 10, 15, 20],
      // feauture: ["WFreq", "WRel", "tf", "WCase", "WPos", "WSpread"],
      ngram: [1, 2, 3, 4, 5],
      text: "",
      textraw: "",
      // lan_req: "vi",
      // feauture_req: ["WRel", "tf"],
      ngram_req: 3,
      headers: [
        {
          text: "Words",
          align: "start",
          sortable: false,
          value: "word"
        },
        { text: "Score", value: "score" }
      ],
      items: []
    };
  },
  computed: {
    ...mapState("text", ["dataRes"])
  },
  methods: {
    ...mapActions("text", ["PostText"]),
    async extractDocument() {
      this.isExtract = false;
      this.text = this.textraw;
      const dataReq = {
        text: this.text,
        lan: this.lan_req,
        ngram: this.ngram_req,
        feauture: this.feauture_req,
        numOfKeyWords: this.noW
      };

      if (this.text === "") {
        this.text = "no data";
      } else {
        const { isSuccess } = await this.PostText(dataReq);
        this.items = this.dataRes.result;
        // for (let index = 0; index < this.items.length; index++) {
        //   this.keywords[index] = this.items[index].word;
        // }
      }
    },
    reload() {
      this.isExtract = true;
      this.textraw = null;
    }
  }
};
</script>

<style>
.my-highlight {
  padding: 0px;
  margin: 0px;
  word-spacing: normal;
  letter-spacing: 1;
  white-space: pre-wrap;
}
</style>