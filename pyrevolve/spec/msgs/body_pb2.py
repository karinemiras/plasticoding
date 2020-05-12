# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: body.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import parameter_pb2 as parameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='body.proto',
  package='revolve.msgs',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\nbody.proto\x12\x0crevolve.msgs\x1a\x0fparameter.proto\"\xb3\x01\n\x08\x42odyPart\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\t\n\x01x\x18\x03 \x02(\x05\x12\t\n\x01y\x18\x04 \x02(\x05\x12\x13\n\x0borientation\x18\x05 \x02(\x01\x12+\n\x05\x63hild\x18\x06 \x03(\x0b\x32\x1c.revolve.msgs.BodyConnection\x12&\n\x05param\x18\x07 \x03(\x0b\x32\x17.revolve.msgs.Parameter\x12\r\n\x05label\x18\x08 \x01(\t\"Z\n\x0e\x42odyConnection\x12\x10\n\x08src_slot\x18\x01 \x02(\x05\x12\x10\n\x08\x64st_slot\x18\x02 \x02(\x05\x12$\n\x04part\x18\x03 \x02(\x0b\x32\x16.revolve.msgs.BodyPart\",\n\x04\x42ody\x12$\n\x04root\x18\x01 \x02(\x0b\x32\x16.revolve.msgs.BodyPart')
  ,
  dependencies=[parameter__pb2.DESCRIPTOR,])




_BODYPART = _descriptor.Descriptor(
  name='BodyPart',
  full_name='revolve.msgs.BodyPart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='revolve.msgs.BodyPart.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='revolve.msgs.BodyPart.type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='revolve.msgs.BodyPart.x', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='revolve.msgs.BodyPart.y', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='revolve.msgs.BodyPart.orientation', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child', full_name='revolve.msgs.BodyPart.child', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='revolve.msgs.BodyPart.param', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='revolve.msgs.BodyPart.label', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=225,
)


_BODYCONNECTION = _descriptor.Descriptor(
  name='BodyConnection',
  full_name='revolve.msgs.BodyConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src_slot', full_name='revolve.msgs.BodyConnection.src_slot', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_slot', full_name='revolve.msgs.BodyConnection.dst_slot', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='part', full_name='revolve.msgs.BodyConnection.part', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=317,
)


_BODY = _descriptor.Descriptor(
  name='Body',
  full_name='revolve.msgs.Body',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root', full_name='revolve.msgs.Body.root', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=363,
)

_BODYPART.fields_by_name['child'].message_type = _BODYCONNECTION
_BODYPART.fields_by_name['param'].message_type = parameter__pb2._PARAMETER
_BODYCONNECTION.fields_by_name['part'].message_type = _BODYPART
_BODY.fields_by_name['root'].message_type = _BODYPART
DESCRIPTOR.message_types_by_name['BodyPart'] = _BODYPART
DESCRIPTOR.message_types_by_name['BodyConnection'] = _BODYCONNECTION
DESCRIPTOR.message_types_by_name['Body'] = _BODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BodyPart = _reflection.GeneratedProtocolMessageType('BodyPart', (_message.Message,), dict(
  DESCRIPTOR = _BODYPART,
  __module__ = 'body_pb2'
  # @@protoc_insertion_point(class_scope:revolve.msgs.BodyPart)
  ))
_sym_db.RegisterMessage(BodyPart)

BodyConnection = _reflection.GeneratedProtocolMessageType('BodyConnection', (_message.Message,), dict(
  DESCRIPTOR = _BODYCONNECTION,
  __module__ = 'body_pb2'
  # @@protoc_insertion_point(class_scope:revolve.msgs.BodyConnection)
  ))
_sym_db.RegisterMessage(BodyConnection)

Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), dict(
  DESCRIPTOR = _BODY,
  __module__ = 'body_pb2'
  # @@protoc_insertion_point(class_scope:revolve.msgs.Body)
  ))
_sym_db.RegisterMessage(Body)


# @@protoc_insertion_point(module_scope)
