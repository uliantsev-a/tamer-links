
import ComponentBase from '@/components/base/base.vue'
import linkForm from '@/components/linkForm/linkForm.vue'
import * as types from '@/store/mutation-types'

export default {
  components: {
    ComponentBase,
    linkForm
  },
  data () {
    return {
      hostname: window.location.hostname + '/',
      location: `${window.location.protocol}//${window.location.hostname}${(window.location.port ? ":" + window.location.port : "/")}`

    }
  },
  created () {
    this.$store.dispatch(types.RESOURCES_REQUEST, this.$route.query)
      .catch(err => {
        console.error(err)
      })
  },
  computed: {
    resourcesList () {
      return this.$store.getters.resources
    },
    pagination () {
      return this.$store.getters.pagination
    }
  }
}
