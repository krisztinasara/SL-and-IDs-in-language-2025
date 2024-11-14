library(tidyverse)

df = read_csv("MetaAnalysis-EffectSizes.csv")

glimpse(df)

agl = df |>
  filter(
    `Age Group` == "Adults",
    `Stimuli Modality` == "Auditory",
    `Stimuli Domain` == "Linguistic",
    `SL Test Measure` == "Reflection based",
    ((`General Paradigm` == "AGL") | (`General Paradigm 2` == "AGL")),
    `Pattern Range` == "Adjacent",
    `Language Related Disorder` == "TD",
    `Disorder Population` == "TD",
    `Language Test Category` == "Comprehension"
  )
agl$ES |> mean()

TP = df |>
  filter(
    `Age Group` == "Adults",
    `Stimuli Modality` == "Auditory",
    `Stimuli Domain` == "Linguistic",
    `SL Test Measure` == "Reflection based",
    ((`General Paradigm` == "TP Learning") | (`General Paradigm 2` == "TP Learning")),
    `Pattern Range` == "Adjacent",
    `Language Related Disorder` == "TD",
    `Disorder Population` == "TD",
    ((`Language Test Category` != "Vocabulary") & (`Language Test Category` != "Receptive Vocabulary"))
  )

on = df |>
  filter(
    `Age Group` == "Adults",
    `Stimuli Modality` == "Auditory",
    `Stimuli Domain` == "Linguistic",
    `SL Test Measure` == "Processing based",
    ((`General Paradigm` == "TP Learning") | (`General Paradigm 2` == "TP Learning")),
    `Pattern Range` == "Adjacent",
    `Language Related Disorder` == "TD",
    `Disorder Population` == "TD"
  )

off_all = df |>
  filter(
    `Age Group` == "Adults",
    `SL Test Measure` == "Reflection based",
    #((`General Paradigm` == "TP Learning") | (`General Paradigm 2` == "TP Learning")),
    `Pattern Range` == "Adjacent",
    `Language Related Disorder` == "TD",
    `Disorder Population` == "TD",
    ((`Language Test Category` == "Comprehension") | (`Language Test Category` == "Syntax") | (`Language Test Category` == "Reading") | (`Language Test Category` == "Sentence comprehension, Receptive vocabulary, and Syntax") | (`Language Test Category` == "Receptive grammar abilities"))
  )
off_all$ES |> mean()

on_all = df |>
  filter(
    `Age Group` == "Adults",
    `SL Test Measure` == "Processing based",
    #((`General Paradigm` == "TP Learning") | (`General Paradigm 2` == "TP Learning")),
    `Pattern Range` == "Adjacent",
    `Language Related Disorder` == "TD",
    `Disorder Population` == "TD",
    ((`Language Test Category` == "Comprehension") | (`Language Test Category` == "Syntax") | (`Language Test Category` == "Reading") | (`Language Test Category` == "Sentence comprehension, Receptive vocabulary, and Syntax") | (`Language Test Category` == "Receptive grammar abilities"))
  )
on_all$ES |> mean()

ling = df |>
  filter(
    `Age Group` == "Adults",
    #`Stimuli Modality` == "Auditory",
    `Stimuli Domain` == "Linguistic",
    `Language Related Disorder` == "TD",
    `Disorder Population` == "TD"
  )
ling$ES |> mean()
