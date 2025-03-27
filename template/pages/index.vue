<!-- pages/exams.vue -->
<template>
  <div class="container">
    <h1>Available Exams</h1>
    <div class="list-group" v-if="exams">
      <a v-for="exam in exams" :key="exam.name" class="list-group-item">
        <div class="row">
          <div class="col-md-8">
            <h4 class="list-group-item-heading">{{ exam.name }}</h4>
            <p class="list-group-item-text">
              Minimum Passing Score: {{ exam.min_required }}
            </p>
            <p class="list-group-item-text">
              Questions: {{ exam.max_questions }}
            </p>
          </div>
          <div class="col-md-4 text-right ">
            <NuxtLink :href="{name: 'exam-id' ,params: {id:exam.id}}" class="btn btn-primary mx-2">Start Test</NuxtLink>
            <NuxtLink :href="{name: 'exam-imersive-id' ,params: {id:exam.id}}" class="btn btn-primary">Start Imsersive Test</NuxtLink>
          </div>
        </div>
      </a>
    </div>

    <NuxtLink :href="{name: 'parser' ,}" class="btn btn-primary">parse</NuxtLink>
  </div>

</template>

<script lang="ts" setup>

import type {Exam} from "~/types";

const {data: exams} = useAsyncData(() => $fetch<Exam[]>(`/api/getExams`));


</script>

<style scoped>
/* Add Bootstrap or other styling here */
</style>
