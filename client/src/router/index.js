import Vue from 'vue'
import Router from 'vue-router'
import ComponentBase from '@/components/base/base.vue'
import HomePage from '@/components/home/home.vue'
import * as types from '@/store/mutation-types'
import store from '@/store'
import NotFound from '@/components/NotFound/NotFound.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/(api|docs)',
      abstract: true
      // pass on to server
    },
    {
      path: '/',
      component: ComponentBase,
      children: [
        {
          path: '/',
          name: 'HomePage',
          component: HomePage
        },
        {
          path: '/:name',
          name: 'link',
          beforeEnter: (to, from, next) => {
            store.dispatch(types.LINK_REQUEST, to.params.name)
              // .then(function () {
              //
              // })
              .catch(function (error) {
                console.log(error)
                next()
              })
          },
          component: NotFound
        }
      ]
    }
  ]
})
