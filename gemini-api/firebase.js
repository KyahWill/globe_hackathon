const functions = require('firebase-functions');
const express = require('express');
const index = require('gemini-api/index.js');

exports.app = functions.https.onRequest(index.app);

