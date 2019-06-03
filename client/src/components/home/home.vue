<template lang="pug">
  .content
    linkForm
    .title
      h1 Resource list
    table.base-table
      tr(v-for="resource in resourcesList")
        td {{ resource.source }}
        td
          a.short-link(:href="resource.short_link") http://{{hostname}}{{ resource.short_link }}

    ul.pagination
      li
        a.preva(:href="location + '?page=' + pagination.previous" v-if="pagination.previous") Prev
        a.preva.disable(:href="location" v-if="!pagination.previous") Prev
      li(v-for="n in pagination.pageCount")
        a(:href="location + '?page=' + n") {{ n }}
      li
        a.next(:href="location + '?page=' + pagination.next" v-if="pagination.next") Next
        a.next.disable(:href="location" v-if="!pagination.next") Next
</template>

<script src="./home.js"></script>
<style scoped lang="scss" src="./home.scss"></style>
