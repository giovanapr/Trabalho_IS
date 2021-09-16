from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from is_msgs import common_pb2 as is__msgs_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RequisicaoRobo.proto',
  package='is.robot',
  syntax='proto3',
  serialized_options=b'\n\014com.is.robotP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14RequisicaoRobo.proto\x12\x08is.robot\x1a\x14is_msgs/common.proto\"V\n\x0eRequisicaoRobo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x66unction\x18\x02 \x01(\t\x12&\n\tpositions\x18\x03 \x01(\x0b\x32\x13.is.common.PositionB\x10\n\x0c\x63om.is.robotP\x01\x62\x06proto3'
  ,
  dependencies=[is__msgs_dot_common__pb2.DESCRIPTOR,])




_REQUISICAOROBO = _descriptor.Descriptor(
  name='RequisicaoRobo',
  full_name='is.robot.RequisicaoRobo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='is.robot.RequisicaoRobo.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function', full_name='is.robot.RequisicaoRobo.function', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='positions', full_name='is.robot.RequisicaoRobo.positions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=142,
)

_REQUISICAOROBO.fields_by_name['positions'].message_type = is__msgs_dot_common__pb2._POSITION
DESCRIPTOR.message_types_by_name['RequisicaoRobo'] = _REQUISICAOROBO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequisicaoRobo = _reflection.GeneratedProtocolMessageType('RequisicaoRobo', (_message.Message,), {
  'DESCRIPTOR' : _REQUISICAOROBO,
  '__module__' : 'RequisicaoRobo_pb2'
  # @@protoc_insertion_point(class_scope:is.robot.RequisicaoRobo)
  })
_sym_db.RegisterMessage(RequisicaoRobo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
