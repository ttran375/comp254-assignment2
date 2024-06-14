docker run -e VALIDATE_BASH=false -e VALIDATE_CHECKOV=false -e VALIDATE_EDITORCONFIG=false -e VALIDATE_GITLEAKS=false -e VALIDATE_GOOGLE_JAVA_FORMAT=false -e VALIDATE_JSCPD=false -e VALIDATE_JSON=false -e VALIDATE_MARKDOWN=false -e VALIDATE_NATURAL_LANGUAGE=false -e VALIDATE_XML=false -e FILTER_REGEX_EXCLUDE=test_* -e RUN_LOCAL=true -v "$(pwd)":/tmp/lint github/super-linter
