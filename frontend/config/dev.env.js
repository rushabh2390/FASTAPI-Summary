'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./dev.env')

module.exports = merge(prodEnv, {
  NODE_ENV:  process.env.NODE_ENV || '"development"',
  API_ENDPOINT: process.env.API_ENDPOINT || '"http://localhost:8000"'
})
