<template lang="pug">
  .container-form
    form.create-form(@submit.prevent="validateBeforeSubmit")
      span.form-non.field_errors {{ errors.first('non_field_errors') }}
      .group-form
        .form-item.source(
          @click="setFocus('source')"
          v-bind:class="{'--active': activeField === 'source', '--fill': Boolean(this.source), '--error': this.errors.has('source')}"
        )
          span.form-item__placeholder
            span.form-item__placeholder-text Original URL
          input.form-item__input(
            name="source" id="source" ref="source"
            v-validate="'required'" v-model="source"
            @blur="clearFocus()"
          )
          span.form-item__error {{ errors.first('source') }}
        .form-item(
          @click="setFocus('short_link')"
          v-bind:class="{'--active': activeField === 'short_link', '--fill': Boolean(this.short_link), '--error': this.errors.has('short_link')}"
        )
          span.form-item__placeholder
            span.form-item__placeholder-text Short variant
          input.form-item__input(
            name="short_link" id="short_link" ref="short_link"
            v-model="short_link"
            @blur="clearFocus()"
          )
          span.form-item__error {{ errors.first('short_link') }}
        input.form-item__button(type="submit" value="Request")
</template>

<script src="./linkForm.js"></script>
<style scoped lang="scss" src="./linkForm.scss"></style>
