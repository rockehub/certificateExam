<!-- pages/exams.vue -->
<template>
  <div class="container">
    <h1>Available Exams</h1>
    <div class="list-group">
      <a v-for="exam in exams" :key="exam.name" class="list-group-item">
        <div class="row">
          <div class="col-md-10">
            <h4 class="list-group-item-heading">{{ exam.name }}</h4>
            <p class="list-group-item-text">
              Minimum Passing Score: {{ exam.min_required }}
            </p>
            <p class="list-group-item-text">
              Questions: {{ exam.max_questions }}
            </p>
          </div>
          <div class="col-md-2 text-right">
            <NuxtLink :href="{name: 'exam-id' ,params: {id:exam.id}}" class="btn btn-primary">Start Test</NuxtLink>
          </div>
        </div>
      </a>
    </div>
  </div>

</template>

<script lang="ts" setup>
import data from '@/static/exams.json'

let exams = data


</script>

<style scoped>
/* Add Bootstrap or other styling here */
</style>
