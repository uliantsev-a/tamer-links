import * as types from '@/store/mutation-types'

export default {
  data() {
    return {
      activeField: '',
      source: null, short_link: null
    }
  },
  methods: {
    validateBeforeSubmit () {
        this.$validator.validateAll().then((result) => {
          if (result) {
            this.createLink()
            return;
          }
        })
    },
    createLink (submitEnv) {
        const { source, short_link } = this
        this.$store.dispatch(types.RESOURCES_CREATE, {
          source, short_link
        }).then(() => {
          this.$router.go('/')
        }).catch(err => {
          this.errors.clear();
          Object.entries(this.$store.getters.validate).forEach((field) => {
            field.reduce((key, values) => {
              if (key === 'detail') {
                this.errors.add({field: 'non_field_errors', msg: values})
              } else {
                this.errors.add({field: key, msg: values.join(', ')})
              }
            })
          })
        })
    },
    setFocus: function (currentField) {
      this.activeField = currentField
      this.$refs[currentField].focus()
    },
    clearFocus: function () {
      this.activeField = ''
    },
  }
}
