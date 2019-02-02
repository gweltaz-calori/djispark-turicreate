import turicreate as tc

modelName = 'spark'

model = tc.load_model(modelName + '.model')
model.export_coreml(modelName.title() + 'Classifier.mlmodel')