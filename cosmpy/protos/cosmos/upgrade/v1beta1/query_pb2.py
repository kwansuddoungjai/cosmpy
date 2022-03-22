# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/upgrade/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/upgrade/v1beta1/query.proto\x12\x16\x63osmos.upgrade.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto\"\x19\n\x17QueryCurrentPlanRequest\"F\n\x18QueryCurrentPlanResponse\x12*\n\x04plan\x18\x01 \x01(\x0b\x32\x1c.cosmos.upgrade.v1beta1.Plan\"\'\n\x17QueryAppliedPlanRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"*\n\x18QueryAppliedPlanResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\"9\n\"QueryUpgradedConsensusStateRequest\x12\x13\n\x0blast_height\x18\x01 \x01(\x03\"]\n#QueryUpgradedConsensusStateResponse\x12\x36\n\x18upgraded_consensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any2\xac\x04\n\x05Query\x12\x9e\x01\n\x0b\x43urrentPlan\x12/.cosmos.upgrade.v1beta1.QueryCurrentPlanRequest\x1a\x30.cosmos.upgrade.v1beta1.QueryCurrentPlanResponse\",\x82\xd3\xe4\x93\x02&\x12$/cosmos/upgrade/v1beta1/current_plan\x12\xa5\x01\n\x0b\x41ppliedPlan\x12/.cosmos.upgrade.v1beta1.QueryAppliedPlanRequest\x1a\x30.cosmos.upgrade.v1beta1.QueryAppliedPlanResponse\"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/upgrade/v1beta1/applied_plan/{name}\x12\xd9\x01\n\x16UpgradedConsensusState\x12:.cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateRequest\x1a;.cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateResponse\"F\x82\xd3\xe4\x93\x02@\x12>/cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height}B.Z,github.com/cosmos/cosmos-sdk/x/upgrade/typesb\x06proto3')



_QUERYCURRENTPLANREQUEST = DESCRIPTOR.message_types_by_name['QueryCurrentPlanRequest']
_QUERYCURRENTPLANRESPONSE = DESCRIPTOR.message_types_by_name['QueryCurrentPlanResponse']
_QUERYAPPLIEDPLANREQUEST = DESCRIPTOR.message_types_by_name['QueryAppliedPlanRequest']
_QUERYAPPLIEDPLANRESPONSE = DESCRIPTOR.message_types_by_name['QueryAppliedPlanResponse']
_QUERYUPGRADEDCONSENSUSSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryUpgradedConsensusStateRequest']
_QUERYUPGRADEDCONSENSUSSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryUpgradedConsensusStateResponse']
QueryCurrentPlanRequest = _reflection.GeneratedProtocolMessageType('QueryCurrentPlanRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCURRENTPLANREQUEST,
  '__module__' : 'cosmos.upgrade.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.QueryCurrentPlanRequest)
  })
_sym_db.RegisterMessage(QueryCurrentPlanRequest)

QueryCurrentPlanResponse = _reflection.GeneratedProtocolMessageType('QueryCurrentPlanResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCURRENTPLANRESPONSE,
  '__module__' : 'cosmos.upgrade.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.QueryCurrentPlanResponse)
  })
_sym_db.RegisterMessage(QueryCurrentPlanResponse)

QueryAppliedPlanRequest = _reflection.GeneratedProtocolMessageType('QueryAppliedPlanRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYAPPLIEDPLANREQUEST,
  '__module__' : 'cosmos.upgrade.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.QueryAppliedPlanRequest)
  })
_sym_db.RegisterMessage(QueryAppliedPlanRequest)

QueryAppliedPlanResponse = _reflection.GeneratedProtocolMessageType('QueryAppliedPlanResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYAPPLIEDPLANRESPONSE,
  '__module__' : 'cosmos.upgrade.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.QueryAppliedPlanResponse)
  })
_sym_db.RegisterMessage(QueryAppliedPlanResponse)

QueryUpgradedConsensusStateRequest = _reflection.GeneratedProtocolMessageType('QueryUpgradedConsensusStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUPGRADEDCONSENSUSSTATEREQUEST,
  '__module__' : 'cosmos.upgrade.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateRequest)
  })
_sym_db.RegisterMessage(QueryUpgradedConsensusStateRequest)

QueryUpgradedConsensusStateResponse = _reflection.GeneratedProtocolMessageType('QueryUpgradedConsensusStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUPGRADEDCONSENSUSSTATERESPONSE,
  '__module__' : 'cosmos.upgrade.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateResponse)
  })
_sym_db.RegisterMessage(QueryUpgradedConsensusStateResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/upgrade/types'
  _QUERY.methods_by_name['CurrentPlan']._options = None
  _QUERY.methods_by_name['CurrentPlan']._serialized_options = b'\202\323\344\223\002&\022$/cosmos/upgrade/v1beta1/current_plan'
  _QUERY.methods_by_name['AppliedPlan']._options = None
  _QUERY.methods_by_name['AppliedPlan']._serialized_options = b'\202\323\344\223\002-\022+/cosmos/upgrade/v1beta1/applied_plan/{name}'
  _QUERY.methods_by_name['UpgradedConsensusState']._options = None
  _QUERY.methods_by_name['UpgradedConsensusState']._serialized_options = b'\202\323\344\223\002@\022>/cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height}'
  _QUERYCURRENTPLANREQUEST._serialized_start=157
  _QUERYCURRENTPLANREQUEST._serialized_end=182
  _QUERYCURRENTPLANRESPONSE._serialized_start=184
  _QUERYCURRENTPLANRESPONSE._serialized_end=254
  _QUERYAPPLIEDPLANREQUEST._serialized_start=256
  _QUERYAPPLIEDPLANREQUEST._serialized_end=295
  _QUERYAPPLIEDPLANRESPONSE._serialized_start=297
  _QUERYAPPLIEDPLANRESPONSE._serialized_end=339
  _QUERYUPGRADEDCONSENSUSSTATEREQUEST._serialized_start=341
  _QUERYUPGRADEDCONSENSUSSTATEREQUEST._serialized_end=398
  _QUERYUPGRADEDCONSENSUSSTATERESPONSE._serialized_start=400
  _QUERYUPGRADEDCONSENSUSSTATERESPONSE._serialized_end=493
  _QUERY._serialized_start=496
  _QUERY._serialized_end=1052
# @@protoc_insertion_point(module_scope)
