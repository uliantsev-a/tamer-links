import * as types from '../mutation-types'
import { HTTP } from '@/main.js'

const state = {
  resources: [],
  pagination: {},
  status: '',
  status_desc: '',
  validate: {}
}
const getters = {
  resources: state => state.resources,
  pagination: state => state.pagination,
  statusDescription: state => state.status_desc,
  status: state => state.status,
  validate: state => state.validate
}

const actions = {
  [types.RESOURCES_REQUEST]: ({commit, dispatch}, query) => {
    return new Promise((resolve, reject) => {
      console.info(HTTP)
      HTTP.get('/link', {params: query})
        .then(resp => {
          commit(types.RESOURCES_SUCCESS, resp.data)
          resolve(resp)
        })
        .catch(err => {
          commit(types.RESOURCES_ERROR, err)
          reject(err)
        })
    })
  },
  [types.RESOURCES_CREATE]: ({commit, dispatch}, data) => {
    return new Promise((resolve, reject) => {
      HTTP.post('/link/', data)
        .then(resp => {
          console.log('resources create success')
          resolve(resp)
        })
        .catch(err => {
          commit(types.RESOURCES_ERROR, err)
          reject(err)
        })
    })
  },
  [types.LINK_REQUEST]: ({commit, dispatch}, shortName) => {
    return new Promise((resolve, reject) => {
      HTTP.get(`/link/${shortName}/`)
        .then(resp => {
          window.location = resp.data.source
          // const data = resp.data
          commit(types.LINK_SUCCESS)
          resolve(resp)
        })
        .catch(err => {
          commit(types.LINK_ERROR, err)
          reject(err)
        })
    })
  }
}

// basic mutations, showing loading, success, error to reflect the api call status and the token when loaded
const mutations = {
  [types.RESOURCES_SUCCESS]: (state, data) => {
    state.resources = data.results
    state.pagination = {
      pageCount: data.count_page,
      pageSize: data.page_size,
      count: data.count,
      next: data.next,
      previous: data.previous
    }
  },
  [types.RESOURCES_ERROR]: (state, err) => {
    state.status = 'error'
    state.status_desc = err.request
    let errors
    if (typeof err.request.response === 'string') {
      errors = JSON.parse(err.request.response)
    } else {
      errors = err.request.response
    }
    state.validate = errors
  },
  [types.LINK_SUCCESS]: (state) => {
    console.info('LINK_SUCCESS')
  },
  [types.LINK_ERROR]: (state, err) => {
    state.status = err.request.status
    state.status_desc = err.request
    console.error(err.request)
    if (err.request.status === 404) {
      state.status = err.request.status
    }
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
