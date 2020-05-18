<template>
  <v-layout>
    <v-flex>
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
      <v-row>
        <v-col cols="3">
          <v-select label="Language" :items="lan" v-model="lan_req"></v-select>
        </v-col>
        <v-col cols="3">
          <v-select label="N-gram" :items="ngram" v-model="ngram_req"></v-select>
        </v-col>
        <v-col cols="3">
          <v-select label="Feauture" :items="feauture" v-model="feauture_req" attach multiple></v-select>
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
        <v-col cols="9">
          <v-card v-if="!isExtract">
            <HighlightText class="my-highlight" :queries="keywords">{{ text }}</HighlightText>
          </v-card>
        </v-col>
      </v-row>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  components: {},
  data() {
    return {
      isExtract: true,
      keywords: ["thanh", "cho", "google", "kaggle"],
      lan: ["en", "vi"],
      feauture: ["WFreq", "WRel", "tf", "WCase", "WPos", "WSpread"],
      ngram: [1, 2, 3, 4, 5],
      text: "",
      textraw: "",
      lan_req: "vi",
      feauture_req: ["WRel", "tf"],
      ngram_req: 3,
      headers: [
        {
          text: "Words",
          align: "start",
          sortable: false,
          value: "word"
        },
        { text: "%", value: "percent" }
      ],
      items: [
        { word: "thanh", percent: 0.0001 },
        { word: "ngu", percent: 0.123 }
      ]
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
        feauture: this.feauture_req
      };
      console.log(dataReq);
      if (this.text === "") {
        this.text = "no data";
      } else {
        const { isSuccess } = await this.PostText(dataReq);
        console.log(this.dataRes);
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