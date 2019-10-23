# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserOrgInfoProto.Proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UserOrgInfoProto.Proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\027TomTaw.eWordIMCIS.Proto'),
  serialized_pb=_b('\n\x16UserOrgInfoProto.Proto\"\xfe\x01\n\x10UserOrgInfoProto\x12\x0f\n\x07userUID\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65ptID\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65ptName\x18\x03 \x01(\t\x12\x16\n\x0eorganizationID\x18\x04 \x01(\t\x12\x18\n\x10organizationName\x18\x05 \x01(\t\x12\x16\n\x0eisSuperManager\x18\x06 \x01(\t\x12\x11\n\tloginName\x18\x07 \x01(\t\x12\x10\n\x08userName\x18\x08 \x01(\t\x12\x0e\n\x06workNO\x18\t \x01(\t\x12\x13\n\x0bofficePhone\x18\n \x01(\t\x12\x14\n\x0cprivatePhone\x18\x0b \x01(\t\x12\r\n\x05\x65mail\x18\x0c \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3')
)




_USERORGINFOPROTO = _descriptor.Descriptor(
  name='UserOrgInfoProto',
  full_name='UserOrgInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userUID', full_name='UserOrgInfoProto.userUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deptID', full_name='UserOrgInfoProto.deptID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deptName', full_name='UserOrgInfoProto.deptName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='UserOrgInfoProto.organizationID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='UserOrgInfoProto.organizationName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSuperManager', full_name='UserOrgInfoProto.isSuperManager', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loginName', full_name='UserOrgInfoProto.loginName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='UserOrgInfoProto.userName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workNO', full_name='UserOrgInfoProto.workNO', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='officePhone', full_name='UserOrgInfoProto.officePhone', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='privatePhone', full_name='UserOrgInfoProto.privatePhone', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='UserOrgInfoProto.email', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=281,
)

DESCRIPTOR.message_types_by_name['UserOrgInfoProto'] = _USERORGINFOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserOrgInfoProto = _reflection.GeneratedProtocolMessageType('UserOrgInfoProto', (_message.Message,), {
  'DESCRIPTOR' : _USERORGINFOPROTO,
  '__module__' : 'UserOrgInfoProto.Proto_pb2'
  # @@protoc_insertion_point(class_scope:UserOrgInfoProto)
  })
_sym_db.RegisterMessage(UserOrgInfoProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)