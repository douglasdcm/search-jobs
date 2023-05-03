const spec = {
	"openapi": "3.0.1",
	"info": {
		"title": "Vagas pra mim",
		"description": "API specification",
		"version": "0.1"
	},
	"servers": [{
		"url": "http://localhost:5000"
	}],
	"paths": {
		"/api/receiver": {
			"post": {
				"description": "Search for job positons that match the résumé",
				"requestBody": {
					"content": {
						"application/json": {
							"schema": {
								"type": "object",
								"properties": {
									"condition": {
										"type": "string",
										"description": "Use 'or' for a widely serch; 'and' for a restrict search"
									},
									"message": {
										"type": "string",
										"description": "résumé content"
									}
								}
							},
							"Access-Control-Allow-Origin": "*",
							"examples": {
								"0": {
									"value": "{\n    \"message\": \"python\",\n    \"condition\": \"or\"\n}"
								}
							}
						}
					}
				},
				"responses": {
					"200": {
						"description": "Résumé is similar to some job positions",
						"content": {
							"application/json": {
								"schema": {
									"type": "object",
									"properties": {
										"message": {
											"type": "object",
											"properties": {
												"https://boards.greenhouse.io/tripadvisor/jobs/4813931": {
													"type": "string"
												},
												"http://4alltests.com.br/vaga.php?id=256": {
													"type": "string"
												},
												"http://4alltests.com.br/vaga.php?id=254": {
													"type": "string"
												}
											}
										},
										"status": {
											"type": "string"
										}
									}
								},
								"examples": {
									"0": {
										"value": "{\"status\":\"ok\",\"message\":{\"https://boards.greenhouse.io/tripadvisor/jobs/4962267\":\"13.87\",\"https://boards.greenhouse.io/tripadvisor/jobs/4365621\":\"13.74\",\"https://boards.greenhouse.io/tripadvisor/jobs/4365536\":\"13.61\",\"https://boards.greenhouse.io/tripadvisor/jobs/4813931\":\"13.61\",\"https://boards.greenhouse.io/tripadvisor/jobs/5005542\":\"13.61\",\"https://boards.greenhouse.io/tripadvisor/jobs/4349330\":\"13.48\",\"https://vivo.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ2MzkzNzJ9?jobBoardSource=gupy_public_page\":\"13.48\",\"https://boards.greenhouse.io/tripadvisor/jobs/4999711\":\"13.25\",\"https://cielo.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ0MzIwNzl9?jobBoardSource=gupy_public_page\":\"13.25\",\"https://vivo.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ0NTM5MjB9?jobBoardSource=gupy_public_page\":\"13.25\",\"http://4alltests.com.br/vaga.php?id=269\":\"13.13\",\"https://jobs.sap.com/job/Gliwice-Developer-with-Python-44-100/918024901/\":\"13.13\",\"https://jobs.sap.com/job/Gliwice-Lead-DeveloperArchitect-with-Python-44-100/917979101/\":\"13.13\",\"https://takeblip.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ3MDQzNTF9?jobBoardSource=gupy_public_page\":\"13.02\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ1NDAzODV9?jobBoardSource=gupy_public_page\":\"13.02\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ3Mjk1OTl9?jobBoardSource=gupy_public_page\":\"13.02\",\"http://4alltests.com.br/vaga.php?id=256\":\"12.91\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ0Njk5Njd9?jobBoardSource=gupy_public_page\":\"12.91\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ1MjQwNjN9?jobBoardSource=gupy_public_page\":\"12.91\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ1MzYzODZ9?jobBoardSource=gupy_public_page\":\"12.8\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ2NjI0OTR9?jobBoardSource=gupy_public_page\":\"12.8\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ2NjIzMzB9?jobBoardSource=gupy_public_page\":\"12.8\",\"http://4alltests.com.br/vaga.php?id=254\":\"12.7\",\"https://tech-career.gupy.io/job/eyJzb3VyY2UiOiJndXB5X3B1YmxpY19wYWdlIiwiam9iSWQiOjQ2OTM3ODd9?jobBoardSource=gupy_public_page\":\"12.7\"}}\n"
									}
								}
							}
						}
					}
				},
				"servers": [{
					"url": "http://localhost:5000"
				}]
			},
			"servers": [{
				"url": "http://localhost:5000"
			}]
		},

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