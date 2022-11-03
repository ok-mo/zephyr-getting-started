*** Settings ***
Library  Process

*** Keywords ***

Readme should follow sales letter structure
	Readme should have a niche specific headline
	Readme should contain proof and evidence
	Readme should make it clear who this is for
	Readme should describe the core concept
	Readme should describe the process and steps
	Readme should specify who the offer is for
	Readme should outline benefits and outcomes
	Readme should make an offer with call to action

Rst Should Contain H1 Headline
	[Arguments]  ${RST}  ${HEADLINE}
	${result}=  Run Process
	...  grep  -Pzl
	...  (?s)${HEADLINE}.*\\n\\*\\*\\*\\*\\*.*
	...  ${RST}
	IF  ${result.rc} != 0
		Log To Console  ${result.stderr}
		Log To Console  Headline "${HEADLINE}" not present in "${RST}"
		Fail
	END

Rst Should Contain H2 Headline
	[Arguments]  ${RST}  ${HEADLINE}
	${result}=  Run Process
	...  grep  -Pzl
	...  (?s)${HEADLINE}.*\\n#####.*
	...  ${RST}
	IF  ${result.rc} != 0
		Log To Console  ${result.stderr}
		Log To Console  Subheadline "${HEADLINE}" not present in "${RST}"
		Fail
	END

Readme should have a niche specific headline
	Rst Should Contain H1 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  Swedish Embedded Firmware Platform SDK

Readme should contain proof and evidence
	Rst Should Contain H2 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  Applications built using this SDK

Readme should make it clear who this is for
	Rst Should Contain H2 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  Who this SDK is for

Readme should describe the core concept
	Rst Should Contain H2 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  Concept behind this SDK

Readme should describe the process and steps
	Rst Should Contain H2 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  What is included

Readme should specify who the offer is for
	Rst Should Contain H2 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  Who benefits the most from this SDK

Readme should outline benefits and outcomes
	Rst Should Contain H2 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  Benefits of starting with this SDK

Readme should make an offer with call to action
	Rst Should Contain H2 Headline
		...  ${PROJECT_ROOT}/README.rst
		...  How to get started
