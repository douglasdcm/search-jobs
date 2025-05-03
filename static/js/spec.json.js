const spec = {
	"openapi": "3.0.1",
	"info": {
		"title": "Vagas pra mim",
		"description": "API specification",
		"version": "0.1"
	},
	"servers": [{
		"url": "http://localhost:5001"
	}],
	"paths": {
		"/api/overwrite": {
			"post": {
				"description": "Update the database (cannot be tested on container as it still uses enviroment variables)",
				"requestBody": {
					"content": {
						"application/json": {
							"schema": {
								"type": "object",
								"properties": {
									"password": {
										"type": "string"
									}
								}
							},
							"Access-Control-Allow-Origin": "*",
							"examples": {
								"0": {
									"value": "{\n    \"password\": \"anypassword\"}"
								}
							}
						}
					}
				},
				"responses": {
					"200": {
						"description": "Database updated",
						"content": {
							"application/json": {
								"schema": {
									"type": "object",
									"properties": {
										"message": {
											"type": "object",
											"properties": {
												"{\"status\": \"ok\", \"message\": \"overwrite finished\"}": {
													"type": "object"
												}
											}
										},
										"status": {
											"type": "string"
										}
									}
								},
								"examples": {
									"200 OK": {
										"value": "{\"status\": \"ok\", \"message\": \"overwrite finished\"}"
									},
									"404 NOT FOUND": {
										"value": "{\"status\": \"failed\", \"message\": \"nothing to overwrite\"}"
									}
								}
							}
						}
					}
				}
			}
		},

		"/api/logs": {
			"post": {
				"description": "Get the application log (cannot be tested on container as it still uses enviroment variables)",
				"requestBody": {
					"content": {
						"application/json": {
							"schema": {
								"type": "object",
								"properties": {
									"password": {
										"type": "string"
									}
								}
							},
							"Access-Control-Allow-Origin": "*",
							"examples": {
								"0": {
									"value": "{\n    \"password\": \"anypassword\"}"
								}
							}
						}
					}
				},
				"responses": {
					"200": {
						"description": "Database updated",
						"content": {
							"application/json": {
								"schema": {
									"type": "object",
									"properties": {
										"message": {
											"type": "object",
											"properties": {
												"{\"status\": \"ok\", \"message\": \"2023-04-27 01:46:13 INFO     Serving on http://0.0.0.0:5001\n2023-04-27 01:47:40 INFO     (psycopg2.ProgrammingError) relation 'positions' does not exist\"}": {
													"type": "object"
												}
											}
										},
										"status": {
											"type": "string"
										}
									}
								},
								"examples": {
									"200 OK": {
										"value": "{\"status\": \"ok\", \"message\": \"2023-04-27 01:46:13 INFO     Serving on http://0.0.0.0:5001\n2023-04-27 01:47:40 INFO     (psycopg2.ProgrammingError) relation 'positions' does not exist\"}"
									},
									"404 NOT FOUND": {
										"value": "{\"status\": \"failed\", \"message\": \"nothing to log\"}"
									}
								}
							}
						}
					}
				}
			}
		}
	}
}